# 0537 — Parse an integer

Use the `parsy` parser-combinator library: `regex(r'[0-9]+')` is the digit-run combinator, and `.map(int)` transforms the matched text into a Python `int`. Calling `.parse('42')` runs the combinator on the fixed input and yields the parsed value.

## Run

    python3 main.py
