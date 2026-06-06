# 0411 — Concat Streams

Implement concat: subscribe to the second source only after the first completes; concat [1,2] then [3,4]. The first source's `on_complete` callback triggers the subscription to the second, so emissions stay synchronous and ordered.

## Run

    python3 main.py
