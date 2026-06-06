import reactivex as rx
from reactivex import operators as ops

out = []
rx.of(1, 2, 3, 4).pipe(
    ops.map(lambda x: x * 2)
).subscribe(on_next=lambda v: out.append(v))
print('\n'.join(map(str, out)))
