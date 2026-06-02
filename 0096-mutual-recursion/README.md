# 0096 — Mutual Recursion

Using two mutually recursive functions `isEven` and `isOdd` (each calling the other), report whether `4` and `3` are even, printing `even` and `odd`. `is_even` and `is_odd` call each other, each peeling off one until reaching zero; names resolve at call time, so definition order is fine.

## Run

    python3 main.py
