# 0520 — Finds a counterexample

Run the hypothesis property-testing library programmatically (no test runner) on a deliberately false property: "every non-negative integer is < 100". The `@given(st.integers(min_value=0, max_value=10**6))` strategy generates inputs and hypothesis densely finds a counterexample (some `n >= 100`), raising `AssertionError`. The check runs inside `contextlib.redirect_stdout`/`redirect_stderr` so hypothesis's falsifying-example and shrink report never leak to stdout; only `found` is printed.

## Run

    python3 main.py
