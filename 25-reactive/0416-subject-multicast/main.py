from typing import Callable, List


class Observer:
    def __init__(self, on_next: Callable[[int], None]) -> None:
        self.on_next = on_next

    def next(self, value: int) -> None:
        self.on_next(value)


class Subject:
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def next(self, value: int) -> None:
        for observer in self._observers:
            observer.next(value)


def main() -> None:
    subject = Subject()
    subject.subscribe(Observer(lambda v: print("obs1: {}".format(v))))
    subject.subscribe(Observer(lambda v: print("obs2: {}".format(v))))
    subject.next(1)
    subject.next(2)


if __name__ == "__main__":
    main()
