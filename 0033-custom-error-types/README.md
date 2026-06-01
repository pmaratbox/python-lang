# 0033 — Custom Error Types

Define a custom error, raise it from a `check` that rejects values over `100`, catch it for the input `200`, and print `error: value too large`. A custom exception is just a class extending `Exception`; `raise` throws it and `except TooLargeError as e` catches it by type, with `str(e)` yielding the message passed to the constructor.

## Run

    python3 main.py
