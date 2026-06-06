import reactivex as rx

out = []
rx.of(1, 2, 3).subscribe(
    on_next=lambda v: out.append(str(v)),
    on_completed=lambda: out.append("done"),
)
print("\n".join(out))
