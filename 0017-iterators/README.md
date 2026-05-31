# 0017 — Iterators

Take the numbers 1 through 5, keep the even ones, double each, and add them up — a filter, then a map, then a reduce — printing the final sum. Python's idiomatic tool is the *generator expression*: `n * 2 for n in nums if n % 2 == 0` fuses the map (`n * 2`) and the filter (`if n % 2 == 0`) into one lazy stream, and the builtin `sum()` is the reduce. This reads more naturally than chaining `map()` and `filter()`, and stays lazy — no intermediate list is built.

## Run

    python3 main.py
