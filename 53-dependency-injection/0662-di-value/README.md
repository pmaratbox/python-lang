# 0662 — Inject a value

Uses **dependency-injector** (`DeclarativeContainer`) to register a constant
value `v1` with `providers.Object` and inject it into a `ValueService` via a
`providers.Factory`. Resolving `container.service()` builds the service through
the container, wiring the constant into its constructor; calling `get()` returns
the resolved value `v1`.

## Run

    python3 main.py
