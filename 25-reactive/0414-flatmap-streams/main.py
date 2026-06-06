"""FlatMap (mergeMap): map each outer value to an inner timed stream and
merge all inners concurrently, using a virtual-time scheduler."""

import heapq
from typing import Callable, List, Optional


class Scheduler:
    """Virtual-time scheduler: a priority queue of (time, seq, callback)."""

    def __init__(self) -> None:
        self.now = 0
        self._seq = 0
        self._heap: List[list] = []

    def schedule(self, time: int, cb: Callable[[], None]) -> list:
        token = [time, self._seq, cb, False]  # last field = cancelled
        self._seq += 1
        heapq.heappush(self._heap, token)
        return token

    def cancel(self, token: list) -> None:
        token[3] = True

    def run(self) -> None:
        while self._heap:
            time, _seq, cb, cancelled = heapq.heappop(self._heap)
            if cancelled:
                continue
            self.now = time
            cb()


class Observer:
    def __init__(
        self,
        on_next: Callable[[int], None],
        on_complete: Optional[Callable[[], None]] = None,
    ) -> None:
        self.next = on_next
        self.complete = on_complete or (lambda: None)


def timed_source(scheduler: Scheduler, events: List[tuple]):
    """Return an Observable (subscribe function) that emits each (delay, value)
    at scheduler.now + delay relative to subscription time."""

    def subscribe(observer: Observer) -> None:
        base = scheduler.now
        for delay, value in events:
            def emit(v=value):
                observer.next(v)
            scheduler.schedule(base + delay, emit)

    return subscribe


def flat_map(scheduler: Scheduler, source, project: Callable[[int], object]):
    """mergeMap: for each outer value, subscribe to a projected inner stream
    and merge all inner emissions concurrently (no cancellation)."""

    def subscribe(observer: Observer) -> None:
        def on_outer(value: int) -> None:
            inner = project(value)
            inner(Observer(observer.next))

        source(Observer(on_outer))

    return subscribe


def main() -> None:
    scheduler = Scheduler()

    outer = timed_source(scheduler, [(10, 1), (20, 2)])
    merged = flat_map(
        scheduler,
        outer,
        lambda n: timed_source(scheduler, [(5, n), (30, n * 10)]),
    )

    merged(Observer(lambda v: print(v)))
    scheduler.run()


if __name__ == "__main__":
    main()
