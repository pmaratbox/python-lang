# 0703 — Count unchanged lines

Uses Python's stdlib `difflib` diff library to diff two fixed line-lists `A=[apple, banana, cherry]` and `B=[apple, blueberry, cherry, date]`. `difflib.SequenceMatcher(None, a, b).get_opcodes()` yields tagged ranges; summing the length of every `equal` opcode gives the number of UNCHANGED lines (`apple`, `cherry`), which prints as `2`. The count is LCS-determined, not hardcoded.

## Run

    python3 main.py
