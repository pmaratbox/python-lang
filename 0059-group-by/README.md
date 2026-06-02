# 0059 — Group By

Group the words `one`, `two`, `three` by their length and print each length with its words, in ascending order of length: `3:[one,two] 5:[three]`. `collections.defaultdict(list)` auto-creates an empty list for each new length key, so each word just appends; `sorted(groups)` orders the keys for output.

## Run

    python3 main.py
