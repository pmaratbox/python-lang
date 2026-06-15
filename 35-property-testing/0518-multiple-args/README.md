# 0518 — Multiple arguments

This lesson uses [Hypothesis](https://hypothesis.readthedocs.io/), Python's property-based testing library, run programmatically rather than through a test runner. The `@given(st.integers(), st.integers())` decorator supplies TWO independent integer strategies, so each maps to a function parameter and Hypothesis draws a fresh `(a, b)` pair per example. The property asserts `max(a, b) >= a` and `max(a, b) >= b` across all generated inputs. Calling the decorated function executes the property; no `AssertionError` means it held, so it prints `passed`.

## Run

    python3 main.py
