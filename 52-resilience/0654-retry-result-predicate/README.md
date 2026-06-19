# 0654 — Retry on result

Uses **tenacity** with `retry_if_result` to retry based on the *returned value*
rather than an exception. The operation returns an incrementing counter; the
predicate keeps retrying while the result is `< 3`, so tenacity drives the call
three times and prints the first accepted result, `3`.

## Run

    python3 main.py
