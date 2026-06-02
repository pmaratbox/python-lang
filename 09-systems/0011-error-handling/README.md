# 0011 — Error Handling

Write a `divide(a, b)` that raises on a zero divisor, then call it on `10 / 2`
(prints the result) and `10 / 0` (prints an error). Python uses **exceptions**:
`raise` signals an error and `try` / `except` handles it, with `e` carrying the
message. The built-in `ZeroDivisionError` is raised here explicitly for clarity.

## Run

    python3 main.py
