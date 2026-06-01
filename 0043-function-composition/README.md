# 0043 — Function Composition

Compose `inc` (add one) and `twice` (multiply by two) into one function and apply it to `3`, so `inc(twice(3))` prints `7`. `compose(f, g)` returns a `lambda x: f(g(x))` — a closure capturing both functions — so `compose(inc, twice)` runs `twice` first, then `inc`. Functions are first-class values, passed and returned freely.

## Run

    python3 main.py
