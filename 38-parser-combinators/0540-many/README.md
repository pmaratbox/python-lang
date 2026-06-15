# 0540 — Many (repetition)

Use the `parsy` parser-combinator library: `string('a')` matches a single character and `.many()` is the repetition combinator that applies it zero-or-more times, collecting every match into a list. Running it on the fixed input `'aaaa'` yields a four-element list, and `len(...)` reports how many were parsed.

## Run

    python3 main.py
