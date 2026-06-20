# 0700 — Count removed lines

Uses Python's stdlib `difflib` diff library to diff two fixed line-lists `A=[apple,banana,cherry]` and `B=[apple,blueberry,cherry,date]`. `difflib.SequenceMatcher(None, a, b).get_opcodes()` yields edit opcodes; `delete` and `replace` tags contribute the source slice `a[i1:i2]` to the removed lines. This lesson prints the number of REMOVED lines (`banana`) -> `1`.

## Run

    python3 main.py
