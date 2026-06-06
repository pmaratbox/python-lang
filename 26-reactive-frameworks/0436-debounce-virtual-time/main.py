import reactivex as rx
from reactivex import operators as ops
from reactivex.testing import TestScheduler, ReactiveTest

on_next = ReactiveTest.on_next
on_completed = ReactiveTest.on_completed

scheduler = TestScheduler()
source = scheduler.create_hot_observable(
    on_next(10, "a"),
    on_next(20, "b"),
    on_next(100, "c"),
    on_completed(140),
)


def create():
    return source.pipe(ops.debounce(30, scheduler))


res = scheduler.start(create, created=1, subscribed=2, disposed=1000)
vals = [m.value.value for m in res.messages if m.value.kind == "N"]
print("\n".join(str(v) for v in vals))
