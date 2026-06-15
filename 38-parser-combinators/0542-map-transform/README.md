# 0542 — Map / transform

Use the `parsy` parser-combinator library. The `regex(r'[0-9]+')` combinator matches the digit run, and the `.map(...)` combinator transforms the parsed value: a first `.map(int)` turns the text into an integer, then a second `.map(lambda n: n * 2)` doubles it. Calling `.parse('21')` runs the parser on the fixed input, yielding `21` which is mapped to `42`.

## Run

    python3 main.py
