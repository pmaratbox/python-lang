# 0019 — Recursion

Define a recursive `factorial(n)` that multiplies `n` by `factorial(n - 1)` until it bottoms out at `1`, then print `factorial(5) = 120`. Python has no tail-call optimization and caps the call stack at 1000 frames by default (`sys.setrecursionlimit` raises it), so deep recursion raises `RecursionError`. Integers are arbitrary precision, so `factorial` itself never overflows.

## Run

    python3 main.py
