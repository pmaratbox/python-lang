"""Retry On Error: resubscribe to a source on error up to n times."""

from typing import Callable, Optional


class Observer:
    def __init__(
        self,
        on_next: Callable[[object], None],
        on_error: Callable[[object], None],
        on_complete: Callable[[], None],
    ) -> None:
        self.on_next = on_next
        self.on_error = on_error
        self.on_complete = on_complete


class Observable:
    def __init__(self, subscribe: Callable[[Observer], None]) -> None:
        self._subscribe = subscribe

    def subscribe(self, observer: Observer) -> None:
        self._subscribe(observer)


def retry(source: Observable, n: int) -> Observable:
    def on_subscribe(observer: Observer) -> None:
        remaining = [n]

        def attempt() -> None:
            inner = Observer(
                observer.on_next,
                lambda err: _on_error(err),
                observer.on_complete,
            )

            def _on_error(err: object) -> None:
                if remaining[0] > 0:
                    remaining[0] -= 1
                    attempt()
                else:
                    observer.on_error(err)

            inner.on_error = _on_error
            source.subscribe(inner)

        attempt()

    return Observable(on_subscribe)


def make_source() -> Observable:
    count = [0]

    def on_subscribe(observer: Observer) -> None:
        count[0] += 1
        k = count[0]
        print("attempt " + str(k))
        if k < 3:
            observer.on_error("boom")
        else:
            print("ok")
            observer.on_next(k)
            observer.on_complete()

    return Observable(on_subscribe)


def main() -> None:
    source = make_source()
    retried = retry(source, 2)
    observer = Observer(
        on_next=lambda value: None,
        on_error=lambda err: None,
        on_complete=lambda: None,
    )
    retried.subscribe(observer)


if __name__ == "__main__":
    main()
