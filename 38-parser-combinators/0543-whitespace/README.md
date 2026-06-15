# 0543 — Whitespace handling

Use the `parsy` parser-combinator library: `regex(r'\s*')` is a whitespace combinator, and the sequencing operators `>>` (keep right) and `<<` (keep left) chain it around the integer parser so leading and trailing spaces are skipped while only the parsed `int` is kept. Calling `.parse('  42  ')` runs the combinator on the fixed input.

## Run

    python3 main.py
