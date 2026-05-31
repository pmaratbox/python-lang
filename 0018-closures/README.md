# 0018 — Closures

Build a counter that captures a private count starting at zero; each call to the returned function increments the count and returns it, so calling it twice prints 1 then 2. The inner `increment` closes over `count` from the enclosing scope, but assigning to it needs the `nonlocal` keyword — without it, `count += 1` would create a new local and raise an error. The state lives on after `make_counter` returns, held alive by the closure that references it.

## Run

    python3 main.py
