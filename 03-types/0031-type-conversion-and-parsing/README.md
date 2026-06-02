# 0031 — Type Conversion & Parsing

Parse the string `"42"` into an integer and `"3.5"` into a float, then convert the integer back to a string, printing `int: 42`, `float: 3.5`, and `str: 42`. Python converts with the type constructors: `int("42")`, `float("3.5")`, and `str(n)`. A malformed string raises `ValueError`, and `int` even takes a base — `int("2a", 16)`.

## Run

    python3 main.py
