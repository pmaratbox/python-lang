# 0196 — Error Wrapping

Wrap an inner error "inner" inside an outer context and print the combined message `outer: inner`. Python's `raise ... from` records the wrapped error in `__cause__`.

## Run

    python3 main.py
