from typing import Callable, List


class Subscription:
    def __init__(self) -> None:
        self.closed = False

    def unsubscribe(self) -> None:
        self.closed = True


class Observable:
    def __init__(self, producer: Callable[["Observer"], None]) -> None:
        self._producer = producer

    def subscribe(self, make_on_next: Callable[[Subscription], Callable[[int], None]]) -> Subscription:
        sub = Subscription()
        on_next = make_on_next(sub)
        self._producer(Observer(on_next, sub))
        return sub


class Observer:
    def __init__(self, on_next: Callable[[int], None], sub: Subscription) -> None:
        self._on_next = on_next
        self._sub = sub

    def next(self, value: int) -> None:
        # Check the closed flag before delivering each value.
        if self._sub.closed:
            return
        self._on_next(value)


def of(values: List[int]) -> Observable:
    def producer(observer: Observer) -> None:
        for v in values:
            if observer._sub.closed:
                break
            observer.next(v)

    return Observable(producer)


def main() -> None:
    source = of([1, 2, 3, 4])

    def make_on_next(sub: Subscription) -> Callable[[int], None]:
        def on_next(value: int) -> None:
            print(value)
            # Unsubscribe after receiving 2 so later values are not delivered.
            if value == 2:
                sub.unsubscribe()

        return on_next

    source.subscribe(make_on_next)


if __name__ == "__main__":
    main()
