# 0173 — Trie

Insert "cat" and "car" into a trie, then search "car" (yes) and "can" (no), printing `yes no`. Each node uses a `children` dict and an `end` flag, with `dict.setdefault` building the path.

## Run

    python3 main.py
