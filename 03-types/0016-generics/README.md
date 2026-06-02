# 0016 — Generics

Define a generic `first` function that returns the first element of a list, then call it on a list of integers and a list of strings to show one definition working at two types. Python is dynamically typed, so the function is already generic at runtime; generics are expressed in the *type hints* with a `TypeVar`. Declaring `T = TypeVar("T")` and annotating `first(items: list[T]) -> T` tells a type checker that the element type flows through unchanged, while the running code is just `items[0]`. (Python 3.12+ adds the inline `def first[T](...)` syntax; the `TypeVar` form works on every version.)

## Run

    python3 main.py
