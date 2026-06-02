# 0089 — Quicksort

Sort the list `3, 1, 4, 1, 5, 2` using quicksort (partition around a pivot, then recurse on each side) and print the result: `1 1 2 3 4 5`. The first element is the pivot; the rest is split into smaller and not-smaller, each sorted recursively, then concatenated around the pivot (`>=` keeps duplicates).

## Run

    python3 main.py
