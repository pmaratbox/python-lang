# 0701 — Added line content

Uses Python's standard-library `difflib` (`SequenceMatcher.get_opcodes`) to diff two fixed line-lists A and B. Each `insert`/`replace` opcode contributes the target slice `b[j1:j2]`, so the added lines are collected in document (B) order and printed comma-joined.

## Run

    python3 main.py
