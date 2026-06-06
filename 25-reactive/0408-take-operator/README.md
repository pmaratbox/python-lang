# 0408 — Take Operator

Implement take(n) over an unbounded source of the natural numbers, emitting the first 3 then completing (and unsubscribing the source). The source installs its teardown into a shared Subscription before emitting, so on_next can stop the synchronous infinite loop the moment the count is reached.

## Run

    python3 main.py
