from typing import Callable


def inc(x: int) -> int:
    return x + 1


def double(x: int) -> int:
    return x * 2


def apply(f: Callable[[int], int], x: int) -> int:
    return f(x)


print(f"inc 5 = {apply(inc, 5)}")
print(f"double 5 = {apply(double, 5)}")
