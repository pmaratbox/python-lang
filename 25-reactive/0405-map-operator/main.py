"""Map operator: transform each emitted value with a function."""

from typing import Any, Callable, Optional


class Observer:
    def __init__(
        self,
        on_next: Callable[[Any], None],
        on_error: Optional[Callable[[Any], None]] = None,
        on_complete: Optional[Callable[[], None]] = None,
    ) -> None:
        self.on_next = on_next
        self.on_error = on_error
        self.on_complete = on_complete

    def next(self, value: Any) -> None:
        self.on_next(value)

    def error(self, err: Any) -> None:
        if self.on_error is not None:
            self.on_error(err)

    def complete(self) -> None:
        if self.on_complete is not None:
            self.on_complete()


class Observable:
    def __init__(self, subscribe: Callable[[Observer], None]) -> None:
        self._subscribe = subscribe

    def subscribe(self, observer: Observer) -> None:
        self._subscribe(observer)


def from_values(values) -> Observable:
    def subscribe(observer: Observer) -> None:
        for value in values:
            observer.next(value)
        observer.complete()

    return Observable(subscribe)


def map_op(source: Observable, f: Callable[[Any], Any]) -> Observable:
    def subscribe(observer: Observer) -> None:
        inner = Observer(
            on_next=lambda value: observer.next(f(value)),
            on_error=observer.error,
            on_complete=observer.complete,
        )
        source.subscribe(inner)

    return Observable(subscribe)


def main() -> None:
    source = from_values([1, 2, 3, 4])
    doubled = map_op(source, lambda x: x * 2)
    doubled.subscribe(Observer(on_next=lambda value: print(value)))


if __name__ == "__main__":
    main()
