from typing import Any, Callable, List, Optional


class Observer:
    def __init__(
        self,
        on_next: Callable[[Any], None],
        on_error: Optional[Callable[[Exception], None]] = None,
        on_complete: Optional[Callable[[], None]] = None,
    ) -> None:
        self.on_next = on_next
        self.on_error = on_error or (lambda e: None)
        self.on_complete = on_complete or (lambda: None)


class ReplaySubject:
    """A subject that buffers the last `buffer_size` values and replays them
    to any late subscriber before forwarding subsequent values."""

    def __init__(self, buffer_size: int) -> None:
        self.buffer_size = buffer_size
        self.buffer: List[Any] = []
        self.observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        # Replay the buffered values to the late subscriber first.
        for value in self.buffer:
            observer.on_next(value)
        self.observers.append(observer)

    def next(self, value: Any) -> None:
        self.buffer.append(value)
        if len(self.buffer) > self.buffer_size:
            self.buffer = self.buffer[-self.buffer_size :]
        for observer in self.observers:
            observer.on_next(value)


def main() -> None:
    subject = ReplaySubject(buffer_size=2)

    # Emit before any subscriber exists; buffer keeps the last 2 -> [2, 3].
    subject.next(1)
    subject.next(2)
    subject.next(3)

    # Late subscriber: immediately receives buffered 2, 3.
    subject.subscribe(Observer(on_next=lambda v: print(v)))

    # New value reaches the subscriber too.
    subject.next(4)


if __name__ == "__main__":
    main()
