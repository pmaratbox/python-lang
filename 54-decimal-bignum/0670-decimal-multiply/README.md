# 0670 — Exact decimal multiplication

Uses Python's stdlib `decimal.Decimal` (an exact base-10 decimal type) to multiply
`1.1 * 1.1`. Unlike binary `float`, `Decimal` keeps the value exact, so the product
is exactly `1.21` with no rounding error.

## Run

    python3 main.py
