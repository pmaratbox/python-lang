# 0516 — Sort is idempotent

Uses the [hypothesis](https://hypothesis.readthedocs.io/) property-testing library: the `@given(st.lists(st.integers()))` generator feeds ~100 random integer lists into the property `sorted(sorted(xs)) == sorted(xs)`, checked programmatically by calling the decorated function. Since no `AssertionError` is raised, the program prints `passed`.

## Run

    python3 main.py
