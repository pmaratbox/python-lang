# 0053 — Binary Search

Binary-search the sorted array `1, 3, 5, 7, 9` for `7` and print the index where it is found: `found 7 at index 3`. The loop halves the `[lo, hi]` window each step, comparing the midpoint. The stdlib equivalent is the `bisect` module (`bisect_left` finds the insertion point in O(log n)).

## Run

    python3 main.py
