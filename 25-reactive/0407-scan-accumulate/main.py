from typing import Any, Callable, List, Optional


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
    def __init__(self, producer: Callable[[Observer], None]) -> None:
        self._producer = producer

    def subscribe(self, observer: Observer) -> None:
        self._producer(observer)


def from_iterable(values: List[Any]) -> Observable:
    def producer(observer: Observer) -> None:
        for v in values:
            observer.next(v)
        observer.complete()

    return Observable(producer)


def scan(source: Observable, acc: Any, f: Callable[[Any, Any], Any]) -> Observable:
    def producer(observer: Observer) -> None:
        state = {"value": acc}

        def on_next(value: Any) -> None:
            state["value"] = f(state["value"], value)
            observer.next(state["value"])

        source.subscribe(Observer(on_next, observer.error, observer.complete))

    return Observable(producer)


def main() -> None:
    source = from_iterable([1, 2, 3, 4])
    running_sums = scan(source, 0, lambda state, value: state + value)
    running_sums.subscribe(Observer(lambda v: print(v)))


if __name__ == "__main__":
    main()
