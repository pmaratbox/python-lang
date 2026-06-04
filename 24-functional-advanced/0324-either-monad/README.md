# 0324 — Either Monad

Chain Either computations: a successful divide chain yields 2, and a divide-by-zero yields an error, printing `2 err`. `bind` propagates a `Left` unchanged so the failing chain stops at the error.

## Run

    python3 main.py
