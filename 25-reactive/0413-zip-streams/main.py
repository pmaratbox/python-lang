"""Zip two push-based observables, pairing values by index."""

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


class Observable:
    def __init__(self, producer: Callable[[Observer], None]) -> None:
        self._producer = producer

    def subscribe(self, observer: Observer) -> None:
        self._producer(observer)


def from_iterable(values: List[Any]) -> Observable:
    def producer(observer: Observer) -> None:
        for v in values:
            observer.on_next(v)
        observer.on_complete()

    return Observable(producer)


def zip_streams(
    a: Observable, b: Observable, combine: Callable[[Any, Any], Any]
) -> Observable:
    """Buffer each source; whenever both queues are non-empty, emit combine."""

    def producer(observer: Observer) -> None:
        queue_a: List[Any] = []
        queue_b: List[Any] = []

        def drain() -> None:
            while queue_a and queue_b:
                x = queue_a.pop(0)
                y = queue_b.pop(0)
                observer.on_next(combine(x, y))

        a.subscribe(
            Observer(
                on_next=lambda x: (queue_a.append(x), drain()) and None,
            )
        )
        b.subscribe(
            Observer(
                on_next=lambda y: (queue_b.append(y), drain()) and None,
            )
        )
        observer.on_complete()

    return Observable(producer)


def main() -> None:
    a = from_iterable([1, 2, 3])
    b = from_iterable([10, 20, 30])
    zipped = zip_streams(a, b, lambda x, y: x + y)
    zipped.subscribe(Observer(on_next=lambda v: print(v)))


if __name__ == "__main__":
    main()
