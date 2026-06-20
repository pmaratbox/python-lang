# 0705 — Identical inputs

Uses Python's stdlib [`difflib`](https://docs.python.org/3/library/difflib.html) library to diff two fixed line-lists. `difflib.SequenceMatcher(None, a, b).get_opcodes()` yields `(tag, i1, i2, j1, j2)` tuples; `insert`/`replace` tags contribute `added` lines and `delete`/`replace` tags contribute `removed` lines. Here both inputs are identical (A->A), so every opcode is `equal`: there are no added or removed lines, and we print the two counts `0 0`.

## Run

    python3 main.py
