"""SwitchMap over a from-scratch push-based Observable with a virtual-time scheduler."""

import heapq
from typing import Callable, List, Optional


class Scheduler:
    def __init__(self) -> None:
        self.clock = 0
        self.seq = 0
        self.queue: List[list] = []  # entries: [time, seq, callback, alive]

    def schedule(self, time: int, callback: Callable[[], None]) -> list:
        token = [time, self.seq, callback, True]
        self.seq += 1
        heapq.heappush(self.queue, token)
        return token

    def cancel(self, token: Optional[list]) -> None:
        if token is not None:
            token[3] = False

    def run(self) -> None:
        while self.queue:
            time, _seq, callback, alive = heapq.heappop(self.queue)
            if not alive:
                continue
            self.clock = time
            callback()


class Observer:
    def __init__(self, on_next: Callable[[int], None]) -> None:
        self.on_next = on_next


def make_source(scheduler: Scheduler, events: List[tuple]) -> Callable:
    """Returns subscribe(observer) -> list of scheduled tokens (the subscription)."""

    def subscribe(observer: Observer) -> List[list]:
        tokens: List[list] = []
        for delay, value in events:
            tokens.append(
                scheduler.schedule(
                    scheduler.clock + delay,
                    lambda v=value: observer.on_next(v),
                )
            )
        return tokens

    return subscribe


def switch_map(scheduler: Scheduler, outer: Callable, project: Callable) -> Callable:
    def subscribe(observer: Observer) -> None:
        current: List[List[list]] = [[]]  # current inner subscription tokens

        def on_outer(value: int) -> None:
            # cancel previous inner subscription before starting the new one
            for token in current[0]:
                scheduler.cancel(token)
            inner = project(value)
            current[0] = inner(Observer(observer.on_next))

        outer(Observer(on_outer))

    return subscribe


def main() -> None:
    scheduler = Scheduler()

    outer = make_source(scheduler, [(10, 1), (20, 2)])

    def project(n: int) -> Callable:
        return make_source(scheduler, [(5, n), (30, n * 10)])

    result = switch_map(scheduler, outer, project)
    result(Observer(lambda v: print(v)))

    scheduler.run()


if __name__ == "__main__":
    main()
