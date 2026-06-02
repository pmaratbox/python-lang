from typing import TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


ints = [1, 2, 3]
strs = ["a", "b", "c"]

print(f"first int: {first(ints)}")
print(f"first string: {first(strs)}")
