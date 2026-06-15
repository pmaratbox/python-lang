# 0514 — Integer property

Uses the [hypothesis](https://hypothesis.readthedocs.io/) property-based testing library: `st.integers()` generates integer inputs and `@given` drives the property that addition is commutative (`a + b == b + a`). The decorated function is invoked directly to run the check; with no `AssertionError` it prints `passed`.

## Run

    python3 main.py
