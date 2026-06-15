# 0517 — Custom generator

This lesson uses [Hypothesis](https://hypothesis.readthedocs.io/), Python's property-based testing library, run programmatically rather than through a test runner. A custom generator is built with the `map` combinator (`st.integers().map(lambda n: n * 2)`) so every drawn value is an even integer, and the `@given`/`@settings` property asserts that invariant across all generated inputs. Calling the decorated function executes the property; no `AssertionError` means it held, so it prints `passed`.

## Run

    python3 main.py
