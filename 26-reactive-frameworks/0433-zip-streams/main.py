import reactivex as rx
from reactivex import operators as ops

out = []
rx.zip(rx.of(1, 2, 3), rx.of(10, 20, 30)).pipe(
    ops.map(lambda t: t[0] + t[1])
).subscribe(on_next=lambda v: out.append(v))
print('\n'.join(map(str, out)))
