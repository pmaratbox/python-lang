# 0026 — Sets

Build a set from `1, 2, 2, 3` so the duplicate collapses, then print its `size: 3` and whether it contains `2` (`has 2: yes`) and `5` (`has 5: no`). A `{...}` literal builds a `set`, which discards the duplicate `2` on construction; `len` gives the count and `in` tests membership in O(1) average. Sets are unordered and hold only hashable elements.

## Run

    python3 main.py
