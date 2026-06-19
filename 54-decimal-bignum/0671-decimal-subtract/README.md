# 0671 — Exact decimal subtraction

Uses Python's stdlib `decimal.Decimal` (an exact base-10 decimal type) to subtract `1.0 - 0.1`. Unlike binary floats, `Decimal` keeps the value exact, so the result prints as `0.9` rather than `0.8999999999999999`.

## Run

    python3 main.py
