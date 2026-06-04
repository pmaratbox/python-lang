# 0148 — Parse or Default

Parse "42" to 42 and "x" (invalid) to a default 0, printing `42 0`. A `try`/`except ValueError` around `int()` is the idiomatic way to fall back to a default.

## Run

    python3 main.py
