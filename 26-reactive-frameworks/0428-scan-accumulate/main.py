import reactivex as rx
from reactivex import operators as ops

out = []
rx.of(1, 2, 3, 4).pipe(
    ops.scan(lambda acc, x: acc + x, 0)
).subscribe(on_next=lambda v: out.append(v))
print('\n'.join(map(str, out)))
