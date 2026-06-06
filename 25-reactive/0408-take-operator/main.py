"""take(n) over an unbounded source of the natural numbers.

A push-based Observable implemented from scratch: subscribe wires a producer
to an observer (next/error/complete) and installs an unsubscribe callable on
a Subscription the observer can read DURING emission. take(n) forwards the
first n values, then completes and unsubscribes the source so the otherwise
infinite producer stops being driven.
"""

from typing import Callable, Optional


class Subscription:
    """Handle the source installs early so a synchronous, unbounded producer
    can be stopped from inside on_next."""

    def __init__(self) -> None:
        self._unsubscribe: Optional[Callable[[], None]] = None

    def set(self, fn: Callable[[], None]) -> None:
        self._unsubscribe = fn

    def unsubscribe(self) -> None:
        if self._unsubscribe is not None:
            self._unsubscribe()


class Observer:
    def __init__(
        self,
        on_next: Callable[[int], None],
        on_complete: Callable[[], None],
    ) -> None:
        self.on_next = on_next
        self.on_complete = on_complete


# An Observable here is a subscribe function: it accepts an Observer plus a
# Subscription (into which it installs its teardown) and starts producing.
def naturals() -> Callable[[Observer, Subscription], None]:
    """Unbounded source emitting 1, 2, 3, ... while subscribed."""

    def subscribe(observer: Observer, sub: Subscription) -> None:
        active = {"on": True}
        # Install teardown BEFORE emitting so on_next can stop us mid-loop.
        sub.set(lambda: active.__setitem__("on", False))
        value = 0
        while active["on"]:
            value += 1
            observer.on_next(value)

    return subscribe


def take(
    source: Callable[[Observer, Subscription], None], n: int
) -> Callable[[Observer, Subscription], None]:
    def subscribe(observer: Observer, sub: Subscription) -> None:
        count = {"v": 0}

        def on_next(value: int) -> None:
            if count["v"] >= n:
                return
            count["v"] += 1
            observer.on_next(value)
            if count["v"] >= n:
                observer.on_complete()
                sub.unsubscribe()

        source(Observer(on_next, observer.on_complete), sub)

    return subscribe


def main() -> None:
    taken = take(naturals(), 3)
    taken(
        Observer(lambda x: print(x), lambda: print("completed")),
        Subscription(),
    )


if __name__ == "__main__":
    main()
