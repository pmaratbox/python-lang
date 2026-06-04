from typing import Optional


class C:
    def __init__(self, c: int):
        self.c = c


class B:
    def __init__(self, b: Optional[C]):
        self.b = b


class A:
    def __init__(self, b: Optional[B]):
        self.b = b


def read_c(a: Optional[A]) -> int:
    if a is not None and a.b is not None and a.b.b is not None:
        return a.b.b.c
    return 0


present = A(B(C(5)))
absent = A(None)
print(read_c(present), read_c(absent))
