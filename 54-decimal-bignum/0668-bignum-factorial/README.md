# 0668 — Factorial

Uses Python's native `int` type, which is arbitrary-precision (it grows past the machine word size automatically), to compute `30!` exactly via `math.factorial(30)`. The 33-digit result `265252859812191058636308480000000` is far larger than a 64-bit integer can hold, but `int` represents it without overflow or rounding.

## Run

    python3 main.py
