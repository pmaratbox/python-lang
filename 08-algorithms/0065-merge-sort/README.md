# 0065 — Merge Sort

Sort the list `3, 1, 4, 1, 5, 2` using merge sort (recursively split in half, then merge the sorted halves) and print the result: `1 1 2 3 4 5`. `merge_sort` splits the list at the midpoint and recurses on each half; `merge` interleaves the two sorted halves, and `<=` keeps it stable.

## Run

    python3 main.py
