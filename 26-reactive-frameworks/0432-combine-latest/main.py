import reactivex as rx
from reactivex import operators as ops
from reactivex.testing import TestScheduler, ReactiveTest

on_next = ReactiveTest.on_next

scheduler = TestScheduler()
a = scheduler.create_hot_observable(on_next(10, 1), on_next(30, 2))
b = scheduler.create_hot_observable(on_next(20, 10))


def create():
    return rx.combine_latest(a, b).pipe(ops.map(lambda t: f"({t[0]}, {t[1]})"))


res = scheduler.start(create, created=1, subscribed=2, disposed=1000)
vals = [m.value.value for m in res.messages if m.value.kind == 'N']
print('\n'.join(str(v) for v in vals))
