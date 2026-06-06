from typing import Callable, List, Optional


class Observer:
    def __init__(
        self,
        on_next: Callable[[int], None],
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


def from_values(values: List[int]) -> Observable:
    def producer(observer: Observer) -> None:
        for v in values:
            observer.on_next(v)
        observer.on_complete()

    return Observable(producer)


def concat(a: Observable, b: Observable) -> Observable:
    def producer(observer: Observer) -> None:
        def subscribe_b() -> None:
            b.subscribe(
                Observer(
                    on_next=observer.on_next,
                    on_error=observer.on_error,
                    on_complete=observer.on_complete,
                )
            )

        a.subscribe(
            Observer(
                on_next=observer.on_next,
                on_error=observer.on_error,
                on_complete=subscribe_b,
            )
        )

    return Observable(producer)


def main() -> None:
    a = from_values([1, 2])
    b = from_values([3, 4])
    concat(a, b).subscribe(Observer(on_next=lambda v: print(v)))


if __name__ == "__main__":
    main()
