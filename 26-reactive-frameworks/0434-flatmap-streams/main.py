import reactivex as rx
from reactivex import operators as ops
from reactivex.testing import TestScheduler, ReactiveTest

on_next = ReactiveTest.on_next


def main():
    scheduler = TestScheduler()

    outer = scheduler.create_hot_observable(
        on_next(10, 1),
        on_next(20, 2),
    )

    def make_inner(n):
        return scheduler.create_cold_observable(
            on_next(5, n),
            on_next(30, n * 10),
        )

    def create():
        return outer.pipe(ops.flat_map(make_inner))

    res = scheduler.start(create, created=1, subscribed=2, disposed=1000)
    vals = [m.value.value for m in res.messages if m.value.kind == "N"]
    print("\n".join(str(v) for v in vals))


if __name__ == "__main__":
    main()
