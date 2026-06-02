# 0058 — Labeled Break & Continue

Scan the pairs `(i, j)` with `i` and `j` each from `1` to `3`: use a labeled `continue` to skip the rest of a row once `j > i`, and a labeled `break` to stop the whole scan at `i * j == 4`, printing `1,1`, `2,1`, and `stop at 2,2`. Python has no loop labels: the idiom is to factor the nested loops into a function and `return` to break out of all of them, while a plain inner `break` (with nothing after the inner loop) already skips to the next outer iteration.

## Run

    python3 main.py
