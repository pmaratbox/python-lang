# 0513 — First property

Use the hypothesis library to state a property and check it over generated input. The `@given(st.lists(st.integers()))` decorator makes hypothesis generate many integer lists, and `@settings(max_examples=100)` runs about 100 of them. The property — reversing a list twice yields the original — holds for every generated case, so calling the decorated function raises no `AssertionError` and we print `passed`.

## Run

    python3 main.py
