# 0057 — Sieve of Eratosthenes

Use the Sieve of Eratosthenes to find every prime number up to `10` and print them: `2 3 5 7`. A boolean list marks each index prime; starting at `i*i`, every multiple of a prime `i` is struck out, and the outer loop need only reach `√n`. A comprehension collects the survivors.

## Run

    python3 main.py
