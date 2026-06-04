# 0322 — Lazy Filter + Take

From a lazy stream of naturals, filter the even ones and take three, printing `2 4 6`. Python's `filter` is itself lazy, so it composes with `islice` without materializing the stream.

## Run

    python3 main.py
