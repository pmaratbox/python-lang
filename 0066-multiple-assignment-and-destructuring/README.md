# 0066 — Multiple Assignment & Destructuring

Swap two variables (`a = 1`, `b = 2`) with a single multiple-assignment, then unpack the pair `(3, 4)` into two variables — printing `2 1` then `3 4`. `a, b = b, a` assigns from a tuple built on the right, so the swap is simultaneous; `x, y = (3, 4)` unpacks a tuple the same way.

## Run

    python3 main.py
