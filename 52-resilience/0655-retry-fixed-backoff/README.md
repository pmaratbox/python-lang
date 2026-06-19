# 0655 — Fixed backoff

Uses **tenacity** with a `wait_fixed` (fixed/constant backoff) strategy to retry
an operation that is scripted to fail twice and then succeed. A shared counter
records each invocation; because the library keeps retrying on each raised
exception, the operation runs `3` times in total before returning successfully.
The delay is set to zero so the attempt count is observed without any real wait.

## Run

    python3 main.py
