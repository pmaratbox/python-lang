# 0652 — Return a value

Uses **tenacity** (`Retrying` with `stop_after_attempt` and `wait_none`) to retry
a scripted operation that fails once then returns the string `ok`. Instead of
printing the attempt count, this prints the value the retried call returns once it
finally succeeds, showing that the retry wrapper propagates the operation's result.

## Run

    python3 main.py
