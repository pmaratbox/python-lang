import heapq
from typing import Callable, List, Optional, Tuple


class Scheduler:
    """Virtual-time scheduler: a min-heap of (time, seq, callback)."""

    def __init__(self) -> None:
        self.now = 0
        self._seq = 0
        self._queue: List[Tuple[int, int, Callable[[], None]]] = []

    def schedule(self, time: int, cb: Callable[[], None]) -> None:
        heapq.heappush(self._queue, (time, self._seq, cb))
        self._seq += 1

    def run(self) -> None:
        while self._queue:
            time, _, cb = heapq.heappop(self._queue)
            self.now = time
            cb()


class Observer:
    def __init__(self, on_next: Callable[[str], None]) -> None:
        self.next = on_next


def source(scheduler: Scheduler, events: List[Tuple[str, int]]) -> Callable[[Observer], None]:
    def subscribe(observer: Observer) -> None:
        for value, at in events:
            scheduler.schedule(at, lambda v=value: observer.next(v))

    return subscribe


def throttle(scheduler: Scheduler, window: int, upstream: Callable[[Observer], None]) -> Callable[[Observer], None]:
    """Leading-edge throttle: emit, then suppress for `window` ticks."""

    def subscribe(observer: Observer) -> None:
        block_until = 0

        def on_next(value: str) -> None:
            nonlocal block_until
            if scheduler.now >= block_until:
                observer.next(value)
                block_until = scheduler.now + window

        upstream(Observer(on_next))

    return subscribe


def main() -> None:
    scheduler = Scheduler()
    src = source(scheduler, [("a", 10), ("b", 20), ("c", 100), ("d", 110)])
    throttled = throttle(scheduler, 30, src)
    throttled(Observer(print))
    scheduler.run()


if __name__ == "__main__":
    main()
