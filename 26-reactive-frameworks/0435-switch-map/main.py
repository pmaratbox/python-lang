import reactivex as rx
from reactivex import operators as ops
from reactivex.testing import TestScheduler, ReactiveTest

on_next = ReactiveTest.on_next

scheduler = TestScheduler()

# outer emits 1@10, 2@20 (absolute virtual ticks)
outer = scheduler.create_hot_observable(on_next(10, 1), on_next(20, 2))


def inner(n):
    # inner(n) emits n at +5 and n*10 at +30 (relative to inner subscription)
    return rx.merge(
        rx.timer(5, scheduler=scheduler).pipe(ops.map(lambda _: n)),
        rx.timer(30, scheduler=scheduler).pipe(ops.map(lambda _: n * 10)),
    )


def create():
    # switchMap: map each outer value to an inner observable, then switch_latest
    # so a new outer value cancels the previous inner stream.
    return outer.pipe(ops.map(inner), ops.switch_latest())


res = scheduler.start(create, created=1, subscribed=2, disposed=1000)

vals = [m.value.value for m in res.messages if m.value.kind == "N"]
print("\n".join(str(v) for v in vals))
