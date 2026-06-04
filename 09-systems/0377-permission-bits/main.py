bits = 0b101

rwx = "".join(
    ch if bits & (1 << i) else "-"
    for ch, i in (("r", 2), ("w", 1), ("x", 0))
)

print(rwx)
