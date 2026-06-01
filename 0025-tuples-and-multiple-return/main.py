def min_max(a: int, b: int) -> tuple[int, int]:
    return (min(a, b), max(a, b))

lo, hi = min_max(3, 7)
print(f"min: {lo}")
print(f"max: {hi}")
