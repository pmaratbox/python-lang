"""Merge two timed streams using a virtual-time scheduler."""

import heapq
from typing import Callable, List, Optional


class Scheduler:
    """A virtual-time scheduler: a priority queue of (time, seq, callback)."""

    def __init__(self) -> None:
        self._heap: List[tuple] = []
        self._seq = 0
        self.clock = 0

    def schedule(self, time: int, cb: Callable[[], None]) -> List:
        """Enqueue cb at virtual time. Returns a cancel token."""
        token = [False]  # mutable cell; True means cancelled
        heapq.heappush(self._heap, (time, self._seq, cb, token))
        self._seq += 1
        return token

    def cancel(self, token: List) -> None:
        token[0] = True

    def run(self) -> None:
        while self._heap:
            time, _seq, cb, token = heapq.heappop(self._heap)
            if token[0]:
                continue
            self.clock = time
            cb()


class Observer:
    """An observer wraps next/error/complete callbacks."""

    def __init__(
        self,
        on_next: Callable[[int], None],
        on_error: Optional[Callable[[Exception], None]] = None,
        on_complete: Optional[Callable[[], None]] = None,
    ) -> None:
        self.on_next = on_next
        self.on_error = on_error
        self.on_complete = on_complete

    def next(self, value: int) -> None:
        self.on_next(value)

    def error(self, err: Exception) -> None:
        if self.on_error is not None:
            self.on_error(err)

    def complete(self) -> None:
        if self.on_complete is not None:
            self.on_complete()


def timed_source(scheduler: Scheduler, events: List[tuple]) -> Callable[[Observer], None]:
    """Build an Observable that emits each (time, value) at its virtual time."""

    def subscribe(observer: Observer) -> None:
        for time, value in events:
            scheduler.schedule(time, lambda v=value: observer.next(v))

    return subscribe


def merge(*sources: Callable[[Observer], None]) -> Callable[[Observer], None]:
    """Merge sources by subscribing them all to the same observer."""

    def subscribe(observer: Observer) -> None:
        for source in sources:
            source(observer)

    return subscribe


def main() -> None:
    scheduler = Scheduler()

    stream_a = timed_source(scheduler, [(10, 1), (30, 3), (50, 5)])
    stream_b = timed_source(scheduler, [(20, 2), (40, 4), (60, 6)])

    merged = merge(stream_a, stream_b)
    merged(Observer(on_next=lambda v: print(v)))

    scheduler.run()


if __name__ == "__main__":
    main()
