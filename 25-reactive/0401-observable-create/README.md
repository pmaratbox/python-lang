# 0401 — Create an Observable

Build a push-based Observable from scratch that emits 1, 2, 3 to its observer and then completes. In Python the observer is just a dict of callables, and `subscribe` is plain synchronous calls into `next`/`complete`.

## Run

    python3 main.py
