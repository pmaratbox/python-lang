# 0328 — Trampoline

Sum 1..100 with a trampolined recursion that avoids deep stacks, printing `5050`. Each step returns a thunk (a `lambda`) that a `while callable(...)` loop drives, so the Python stack stays flat.

## Run

    python3 main.py
