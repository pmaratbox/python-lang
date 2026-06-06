# 0405 — Map Operator

Implement a map operator that transforms each emitted value, applying x => x*2 to a stream of 1, 2, 3, 4. The map operator wraps the source's observer in an inner observer whose next forwards f(value).

## Run

    python3 main.py
