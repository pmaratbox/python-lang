# 0044 — Generic Constraints

Write a generic `largest(a, b)` that requires an ordered type, then call it on integers (3 and 9) and on strings (apple and pear), printing `9` and `pear`. `TypeVar("T", int, str)` is a *constrained* type variable: `largest` works for `int` or `str` and the checker rejects other types. At runtime Python is duck-typed — `a > b` simply needs the values to be orderable.

## Run

    python3 main.py
