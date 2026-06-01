# 0030 — Variadic Functions

Define a function that accepts a variable number of integer arguments and returns their total, then call it with `1, 2, 3` to print `sum: 6`. A `*args` parameter (`*nums`) collects extra positional arguments into a tuple, which `sum` then reduces. Callers can also splat an existing iterable with `total(*[1, 2, 3])`.

## Run

    python3 main.py
