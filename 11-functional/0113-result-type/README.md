# 0113 — Result / Either Type

Model success and failure with a Result type: safeDiv(10,2) prints `ok: 5` and safeDiv(1,0) prints `err: divide by zero`. Two `namedtuple`s, Ok and Err, stand in for the variants and `isinstance` dispatches on them.

## Run

    python3 main.py
