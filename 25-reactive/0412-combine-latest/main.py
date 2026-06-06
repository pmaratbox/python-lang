"""combineLatest of two timed streams over a virtual-time scheduler."""

import heapq
from typing import Callable, List, Optional, Tuple


class Scheduler:
    """Virtual-time scheduler: a priority queue of (time, seq, callback)."""

    def __init__(self) -> None:
        self._queue: List[Tuple[int, int, Callable[[], None]]] = []
        self._seq = 0
        self._cancelled = set()
        self.now = 0

    def schedule(self, time: int, callback: Callable[[], None]) -> int:
        token = self._seq
        heapq.heappush(self._queue, (time, token, callback))
        self._seq += 1
        return token

    def cancel(self, token: int) -> None:
        self._cancelled.add(token)

    def run(self) -> None:
        while self._queue:
            time, token, callback = heapq.heappop(self._queue)
            if token in self._cancelled:
                continue
            self.now = time
            callback()


class Observer:
    def __init__(self, on_next: Callable[[int], None]) -> None:
        self.on_next = on_next


def timed_source(scheduler: Scheduler, events: List[Tuple[int, int]]):
    """Return an observable that schedules each (time, value) emission."""

    def subscribe(observer: Observer) -> None:
        for time, value in events:
            scheduler.schedule(time, lambda v=value: observer.on_next(v))

    return subscribe


def combine_latest(source_a, source_b):
    """Emit the pair of latest values whenever either source emits."""

    def subscribe(observer: Observer) -> None:
        latest_a: Optional[int] = None
        latest_b: Optional[int] = None

        def emit() -> None:
            if latest_a is not None and latest_b is not None:
                observer.on_next((latest_a, latest_b))

        def on_a(value: int) -> None:
            nonlocal latest_a
            latest_a = value
            emit()

        def on_b(value: int) -> None:
            nonlocal latest_b
            latest_b = value
            emit()

        source_a(Observer(on_a))
        source_b(Observer(on_b))

    return subscribe


def main() -> None:
    scheduler = Scheduler()
    a = timed_source(scheduler, [(1, 1), (3, 2)])
    b = timed_source(scheduler, [(2, 10)])

    combined = combine_latest(a, b)
    combined(Observer(lambda pair: print("({}, {})".format(pair[0], pair[1]))))

    scheduler.run()


if __name__ == "__main__":
    main()
