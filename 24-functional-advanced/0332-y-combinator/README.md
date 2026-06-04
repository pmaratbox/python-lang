# 0332 — Y Combinator

Define factorial via a fixed-point combinator (no named self-recursion) and compute 5!, printing `120`. The applicative-order Y combinator wraps `x(x)` in a `lambda` thunk to stay lazy, and feeds a non-recursive factorial generator its own fixed point.

## Run

    python3 main.py
