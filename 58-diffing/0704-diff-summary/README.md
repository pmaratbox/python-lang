# 0704 — Diff summary

Uses Python's stdlib `difflib` library to diff two fixed line-lists `A -> B` via `difflib.SequenceMatcher(None, a, b).get_opcodes()`. Each opcode tag is summed into deterministic, LCS-determined stats: `insert`/`replace` contribute to *added* (lines from `B`), `delete`/`replace` contribute to *removed* (lines from `A`), and `equal` contributes to *unchanged*. It prints the three counts space-joined as `<added> <removed> <unchanged>`.

## Run

    python3 main.py
