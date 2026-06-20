# 0706 — All lines added

Uses Python's stdlib `difflib` diff library (`difflib.SequenceMatcher`) to diff an empty list against `["x", "y"]`. The opcodes from `get_opcodes()` classify each chunk as `insert`/`replace` (added), `delete`/`replace` (removed), or `equal` (unchanged); diffing from empty yields every target line as added. We print the added count, `2`.

## Run

    python3 main.py
