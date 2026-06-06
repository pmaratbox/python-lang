import reactivex as rx
from reactivex import operators as ops

out = []
rx.of(1, 2, 3, 4, 5, 6).pipe(
    ops.filter(lambda x: x % 2 == 0)
).subscribe(on_next=lambda v: out.append(v))
print('\n'.join(map(str, out)))
