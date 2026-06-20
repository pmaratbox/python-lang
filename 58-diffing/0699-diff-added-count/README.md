# 0699 — Count added lines

Uses Python's stdlib `difflib` library to diff two fixed line-lists, `A=[apple, banana, cherry]` and `B=[apple, blueberry, cherry, date]`. `difflib.SequenceMatcher(None, a, b).get_opcodes()` returns LCS-determined edit operations; the `insert` and `replace` tags contribute target lines as ADDED (`blueberry`, `date`). The program prints the number of added lines.

## Run

    python3 main.py
