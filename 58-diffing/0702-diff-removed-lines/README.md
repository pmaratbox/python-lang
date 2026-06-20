# 0702 — Removed line content

Uses Python's stdlib `difflib` library to diff two fixed line-lists `A=[apple,banana,cherry]` and `B=[apple,blueberry,cherry,date]`. `difflib.SequenceMatcher(None, a, b).get_opcodes()` yields edit opcodes; the source lines from `delete` and `replace` opcodes (`a[i1:i2]`) are the REMOVED lines. They are collected in document (A) order and comma-joined, giving `banana`.

## Run

    python3 main.py
