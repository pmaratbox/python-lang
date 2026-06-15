# 0515 — String property

Uses the [Hypothesis](https://hypothesis.readthedocs.io/) property-testing
library. The `st.text()` strategy generates strings, and `@given` feeds ~100 of
them into a property checked with a plain `assert`: `len(s + s) == 2 * len(s)`.
We run the check programmatically (just call the decorated function) rather than
via a test runner; no `AssertionError` means the property holds, so we print
`passed`.

## Run

    python3 main.py
