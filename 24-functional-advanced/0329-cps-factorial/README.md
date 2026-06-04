# 0329 — CPS Factorial

Compute 5! in continuation-passing style, printing `120`. Each recursive call threads a `lambda` continuation, and the identity continuation extracts the final result.

## Run

    python3 main.py
