# 0032 — Math Functions

Take the square root of `16`, raise `2` to the 10th power, the absolute value of `-5`, and the larger of `3` and `9`, printing `sqrt: 4`, `pow: 1024`, `abs: 5`, and `max: 9`. `math.sqrt` returns a float, so it is cast to `int` for clean output, whereas the builtin `pow(2, 10)` already gives the integer `1024`; `abs` and `max` are builtins too. (`math.pow` would instead return a float `1024.0`.)

## Run

    python3 main.py
