import reactivex as rx
from reactivex import operators as ops


def naturals():
    n = 1
    while True:
        yield n
        n += 1


out = []

# Unbounded source 1, 2, 3, ... -> take the first 3, then complete.
rx.from_iterable(naturals()).pipe(ops.take(3)).subscribe(
    on_next=lambda v: out.append(str(v)),
    on_completed=lambda: out.append("completed"),
)

print("\n".join(out))
