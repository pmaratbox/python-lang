from typing import Any, Callable, List


class Signal:
    """A writable value with a list of subscriber callbacks."""

    def __init__(self, value: Any) -> None:
        self._value = value
        self._subscribers: List[Callable[[], None]] = []

    def subscribe(self, callback: Callable[[], None]) -> None:
        self._subscribers.append(callback)

    def __call__(self) -> Any:
        return self._value

    def set(self, value: Any) -> None:
        self._value = value
        for callback in list(self._subscribers):
            callback()


class Computed:
    """A derived value that recomputes when any read signal changes."""

    def __init__(self, compute: Callable[[], Any], *deps: Signal) -> None:
        self._compute = compute
        self._cache = compute()
        for dep in deps:
            dep.subscribe(self._recompute)

    def _recompute(self) -> None:
        self._cache = self._compute()

    def __call__(self) -> Any:
        return self._cache


def main() -> None:
    a = Signal(2)
    b = Signal(3)
    total = Computed(lambda: a() + b(), a, b)

    print(total())  # 5
    a.set(10)
    print(total())  # 13


if __name__ == "__main__":
    main()
