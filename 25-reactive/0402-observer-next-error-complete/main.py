from typing import Any, Callable, Optional


class Observer:
    """Wraps next/error/complete and enforces the next*-then-terminal contract.

    A `stopped` flag is set on the first terminal (complete or error); after
    that, next() and any further terminals become no-ops.
    """

    def __init__(
        self,
        on_next: Callable[[Any], None],
        on_error: Optional[Callable[[Any], None]] = None,
        on_complete: Optional[Callable[[], None]] = None,
    ) -> None:
        self._on_next = on_next
        self._on_error = on_error
        self._on_complete = on_complete
        self._stopped = False

    def next(self, value: Any) -> None:
        if self._stopped:
            return
        self._on_next(value)

    def error(self, err: Any) -> None:
        if self._stopped:
            return
        self._stopped = True
        if self._on_error is not None:
            self._on_error(err)

    def complete(self) -> None:
        if self._stopped:
            return
        self._stopped = True
        if self._on_complete is not None:
            self._on_complete()


def main() -> None:
    observer = Observer(
        on_next=lambda value: print(value),
        on_complete=lambda: print("complete"),
    )

    observer.next(1)
    observer.next(2)
    observer.complete()
    observer.next(3)  # ignored: arrives after the terminal


if __name__ == "__main__":
    main()
