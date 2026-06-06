from typing import Any, Callable, Optional


class Observer:
    def __init__(
        self,
        on_next: Callable[[Any], None],
        on_error: Callable[[Exception], None],
        on_complete: Callable[[], None],
    ) -> None:
        self.on_next = on_next
        self.on_error = on_error
        self.on_complete = on_complete


Subscribe = Callable[[Observer], None]


def from_values_then_error(values, err: Exception) -> Subscribe:
    def subscribe(observer: Observer) -> None:
        for v in values:
            observer.on_next(v)
        observer.on_error(err)

    return subscribe


def from_values(values) -> Subscribe:
    def subscribe(observer: Observer) -> None:
        for v in values:
            observer.on_next(v)
        observer.on_complete()

    return subscribe


def catch_error(source: Subscribe, fallback: Subscribe) -> Subscribe:
    def subscribe(observer: Observer) -> None:
        def on_error(_err: Exception) -> None:
            fallback(observer)

        source(Observer(observer.on_next, on_error, observer.on_complete))

    return subscribe


def main() -> None:
    source = from_values_then_error([1, 2], RuntimeError("boom"))
    fallback = from_values([9])
    stream = catch_error(source, fallback)

    stream(
        Observer(
            on_next=lambda v: print(v),
            on_error=lambda e: None,
            on_complete=lambda: None,
        )
    )


if __name__ == "__main__":
    main()
