# 0080 — Deduplicate

Remove duplicates from `1, 2, 2, 3, 1`, keeping the first occurrence of each in order, and print `1 2 3`. `dict.fromkeys` builds a dict whose keys are the values in first-seen order (dicts preserve insertion order), then `list` extracts them.

## Run

    python3 main.py
