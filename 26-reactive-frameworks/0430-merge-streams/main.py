import reactivex as rx
from reactivex.testing import TestScheduler, ReactiveTest

on_next = ReactiveTest.on_next

scheduler = TestScheduler()
a = scheduler.create_hot_observable(
    on_next(10, 1), on_next(30, 3), on_next(50, 5)
)
b = scheduler.create_hot_observable(
    on_next(20, 2), on_next(40, 4), on_next(60, 6)
)


def create():
    return rx.merge(a, b)


res = scheduler.start(create, created=1, subscribed=2, disposed=1000)
vals = [m.value.value for m in res.messages if m.value.kind == 'N']
print('\n'.join(str(v) for v in vals))
