# 0024 — Sorting & Comparators

Sort `[3, 1, 2]` ascending, then again with a custom comparator that reverses the order, printing `asc: 1 2 3` and `desc: 3 2 1`. `sorted` returns a new list and takes a `key=` function (not a two-argument comparator); `reverse=True` flips the result. An old-style comparator can be adapted with `functools.cmp_to_key`, and the in-place variant is `list.sort`.

## Run

    python3 main.py
