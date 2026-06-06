from typing import Callable, List


class Observable:
    """A minimal push-based observable: subscribe wires a producer to an observer."""

    def __init__(self, producer: Callable[["Observer"], None]) -> None:
        self._producer = producer

    def subscribe(self, observer: "Observer") -> None:
        self._producer(observer)


class Observer:
    def __init__(self, on_next: Callable[[int], None]) -> None:
        self.on_next = on_next
        self.on_complete = lambda: None


def of(values: List[int]) -> Observable:
    def producer(observer: Observer) -> None:
        for value in values:
            observer.on_next(value)
        observer.on_complete()

    return Observable(producer)


def filter_op(source: Observable, pred: Callable[[int], bool]) -> Observable:
    """Forward a value only when pred(value) is true."""

    def producer(observer: Observer) -> None:
        inner = Observer(lambda value: observer.on_next(value) if pred(value) else None)
        inner.on_complete = observer.on_complete
        source.subscribe(inner)

    return Observable(producer)


def main() -> None:
    source = of([1, 2, 3, 4, 5, 6])
    evens = filter_op(source, lambda value: value % 2 == 0)
    evens.subscribe(Observer(print))


if __name__ == "__main__":
    main()
