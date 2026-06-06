import heapq
from typing import Callable, List, Optional, Tuple


class Scheduler:
    """A virtual-time scheduler: a priority queue of (time, seq, callback)."""

    def __init__(self) -> None:
        self.clock = 0
        self._seq = 0
        self._heap: List[Tuple[int, int, Callable[[], None]]] = []
        self._cancelled = set()

    def schedule(self, time: int, cb: Callable[[], None]) -> int:
        token = self._seq
        heapq.heappush(self._heap, (time, token, cb))
        self._seq += 1
        return token

    def cancel(self, token: Optional[int]) -> None:
        if token is not None:
            self._cancelled.add(token)

    def run(self) -> None:
        while self._heap:
            time, token, cb = heapq.heappop(self._heap)
            if token in self._cancelled:
                continue
            self.clock = time
            cb()


class Observer:
    def __init__(self, on_next: Callable[[str], None],
                 on_complete: Callable[[], None]) -> None:
        self.next = on_next
        self.complete = on_complete


def source(scheduler: Scheduler,
           events: List[Tuple[str, int]],
           end: int) -> Callable[[Observer], None]:
    def subscribe(observer: Observer) -> None:
        for value, t in events:
            scheduler.schedule(t, lambda v=value: observer.next(v))
        scheduler.schedule(end, observer.complete)
    return subscribe


def debounce(scheduler: Scheduler, window: int,
             upstream: Callable[[Observer], None]) -> Callable[[Observer], None]:
    def subscribe(observer: Observer) -> None:
        pending = {"token": None, "value": None}

        def emit() -> None:
            observer.next(pending["value"])
            pending["token"] = None

        def on_next(value: str) -> None:
            scheduler.cancel(pending["token"])
            pending["value"] = value
            pending["token"] = scheduler.schedule(scheduler.clock + window, emit)

        def on_complete() -> None:
            observer.complete()

        upstream(Observer(on_next, on_complete))
    return subscribe


def main() -> None:
    scheduler = Scheduler()
    src = source(scheduler, [("a", 10), ("b", 20), ("c", 100)], end=100)
    debounced = debounce(scheduler, 30, src)
    debounced(Observer(lambda v: print(v), lambda: None))
    scheduler.run()


if __name__ == "__main__":
    main()
