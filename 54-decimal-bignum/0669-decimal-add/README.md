# 0669 — Exact decimal addition

Uses Python's stdlib `decimal.Decimal`, an exact base-10 decimal type, to add
`0.1 + 0.2`. Unlike binary `float` (which yields `0.30000000000000004`),
`Decimal` represents the values exactly and the addition gives `0.3`.

## Run

    python3 main.py
