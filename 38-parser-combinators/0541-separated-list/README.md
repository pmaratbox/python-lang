# 0541 — Separated list

Use the `parsy` parser-combinator library: an `integer` combinator (`regex(r'[0-9]+').map(int)`) is combined with the `.sep_by(string(','))` combinator, which parses a list of integers separated by `,`. Calling `.parse('1,2,3')` runs the combinator on the fixed input and yields `[1, 2, 3]`, which is then summed to print `6`.

## Run

    python3 main.py
