# 0672 — Exact decimal comparison

Uses Python's stdlib `decimal.Decimal` (an exact base-10 decimal type) to check whether `0.1 + 0.2` equals `0.3`. With binary floats this comparison is `False` (the sum is `0.30000000000000004`), but `Decimal` keeps the arithmetic exact, so the equality holds and prints lowercase as `true`.

## Run

    python3 main.py
