"""Cold vs hot observable, push-based, implemented from scratch."""
from typing import Callable, List


class Observer:
    def __init__(self, on_next: Callable[[int], None]) -> None:
        self.on_next = on_next


class ColdObservable:
    """Each subscription re-runs the producer independently."""

    def __init__(self, producer: Callable[[Observer], None]) -> None:
        self._producer = producer

    def subscribe(self, observer: Observer) -> None:
        self._producer(observer)


class HotObservable:
    """A single shared producer; emissions are multicast to current subscribers."""

    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def emit(self, value: int) -> None:
        for observer in list(self._observers):
            observer.on_next(value)


def cold_producer(observer: Observer) -> None:
    for value in (1, 2, 3):
        observer.on_next(value)


def main() -> None:
    cold = ColdObservable(cold_producer)

    cold_a: List[int] = []
    cold_b: List[int] = []
    cold.subscribe(Observer(cold_a.append))
    cold.subscribe(Observer(cold_b.append))

    hot = HotObservable()
    hot_a: List[int] = []
    hot_b: List[int] = []

    hot.subscribe(Observer(hot_a.append))  # A subscribes first
    hot.emit(1)                            # then producer emits 1 (only A)
    hot.subscribe(Observer(hot_b.append))  # B subscribes late, misses 1
    hot.emit(2)                            # both receive 2
    hot.emit(3)                            # both receive 3

    print("cold A:", " ".join(map(str, cold_a)))
    print("cold B:", " ".join(map(str, cold_b)))
    print("hot A:", " ".join(map(str, hot_a)))
    print("hot B:", " ".join(map(str, hot_b)))


if __name__ == "__main__":
    main()
