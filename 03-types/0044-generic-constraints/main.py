from typing import TypeVar

T = TypeVar("T", int, str)

def largest(a: T, b: T) -> T:
    return a if a > b else b

print(largest(3, 9))
print(largest("apple", "pear"))
