# 0037 — Operator Overloading

Define how `+` (or an `add` method) combines two points, then add `(1, 2)` and `(3, 4)` and print `(4, 6)`. Implementing the `__add__` *dunder* method makes the `+` operator work on `Point`; Python maps each operator to a special method (`__sub__`, `__eq__`, `__mul__`, ...). `__str__` controls how `print` renders it.

## Run

    python3 main.py
