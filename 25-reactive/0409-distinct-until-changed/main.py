"""distinctUntilChanged: drop consecutive duplicate values."""

from typing import Any, Callable, Optional


class Observer:
    def __init__(
        self,
        on_next: Callable[[Any], None],
        on_error: Optional[Callable[[Any], None]] = None,
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

    def distinct_until_changed(self) -> "Observable":
        def producer(downstream: Observer) -> None:
            has_last = {"flag": False}
            last = {"value": None}

            def on_next(value: Any) -> None:
                if not has_last["flag"] or value != last["value"]:
                    has_last["flag"] = True
                    last["value"] = value
                    downstream.on_next(value)

            self.subscribe(Observer(on_next, downstream.on_error, downstream.on_complete))

        return Observable(producer)


def from_iterable(values):
    def producer(observer: Observer) -> None:
        for v in values:
            observer.on_next(v)
        observer.on_complete()

    return Observable(producer)


def main() -> None:
    source = from_iterable([1, 1, 2, 2, 2, 3, 1])
    source.distinct_until_changed().subscribe(Observer(lambda v: print(v)))


if __name__ == "__main__":
    main()
