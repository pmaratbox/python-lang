# 0014 — Higher-Order Functions

Write `apply(f, x)` that calls the function `f` on `x`, then pass it two
different functions, `inc` and `double`. Functions are first-class values in
Python — they can be passed as arguments and named with a `Callable[[int], int]`
type hint. `lambda` would define them inline.

## Run

    python3 main.py
