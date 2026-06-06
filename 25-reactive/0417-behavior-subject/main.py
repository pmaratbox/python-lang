from typing import Callable, List


class Observer:
    def __init__(self, on_next: Callable[[int], None]) -> None:
        self.on_next = on_next


class BehaviorSubject:
    def __init__(self, initial: int) -> None:
        self.current = initial
        self.observers: List[Observer] = []

    def subscribe(self, on_next: Callable[[int], None]) -> Observer:
        observer = Observer(on_next)
        self.observers.append(observer)
        observer.on_next(self.current)
        return observer

    def next(self, value: int) -> None:
        self.current = value
        for observer in self.observers:
            observer.on_next(value)


def main() -> None:
    subject = BehaviorSubject(0)
    subject.subscribe(lambda v: print("A: {}".format(v)))
    subject.next(1)
    subject.subscribe(lambda v: print("B: {}".format(v)))
    subject.next(2)


if __name__ == "__main__":
    main()
