# 0403 — Subscribe and Unsubscribe

Return a Subscription from subscribe() and use it to unsubscribe so later values are not delivered. The synchronous producer checks the Subscription's `closed` flag before each `next`, so calling `unsubscribe()` inside the callback stops delivery immediately.

## Run

    python3 main.py
