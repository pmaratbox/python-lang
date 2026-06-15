# 0519 — Precondition / filter

Constrain generated inputs with a precondition using the hypothesis library. The `@given(st.integers())` decorator generates arbitrary integers, and `assume(n > 0)` acts as a filter: any example failing the precondition is silently discarded so only positive integers reach the assertion `n + 1 > n`. Calling the decorated function runs the check over ~100 valid examples programmatically; with no `AssertionError` raised, the program prints `passed`.

## Run

    python3 main.py
