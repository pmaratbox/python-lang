# 0068 — GCD (Euclid)

Compute the greatest common divisor of `48` and `36` with Euclid's algorithm (repeatedly replace the pair with `(b, a % b)` until the remainder is zero) and print it: `12`. The loop replaces `(a, b)` with `(b, a % b)` until `b` is zero, at which point `a` is the GCD; the tuple assignment makes the update simultaneous.

## Run

    python3 main.py
