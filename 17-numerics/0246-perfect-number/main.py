def is_perfect(n: int) -> bool:
    return sum(d for d in range(1, n) if n % d == 0) == n


def label(n: int) -> str:
    return "yes" if is_perfect(n) else "no"


print("{} {}".format(label(6), label(8)))
