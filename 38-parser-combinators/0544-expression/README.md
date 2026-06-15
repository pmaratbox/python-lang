# 0544 — Expression

Use the `parsy` parser-combinator library: `regex(r'[0-9]+').map(int)` is the integer combinator, and `.sep_by(string('+'), min=1)` is the combinator that parses a `+`-separated sequence of those integers into a list. Mapping `sum` over the result folds the parsed numbers together, so `.parse('10+20+30')` runs the combinator on the fixed input and yields `60`.

## Run

    python3 main.py
