import reactivex as rx

out = []
first = rx.of(1, 2)
second = rx.of(3, 4)
rx.concat(first, second).subscribe(on_next=lambda v: out.append(v))
print('\n'.join(map(str, out)))
