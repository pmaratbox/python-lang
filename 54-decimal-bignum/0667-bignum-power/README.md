# 0667 — Big integer power

Uses Python's native `int` type, which is an arbitrary-precision (bignum) integer, to compute `2 ** 100` exactly. The result has 31 digits and far exceeds any fixed-width machine integer, yet Python computes and prints every digit without overflow or rounding.

## Run

    python3 main.py
