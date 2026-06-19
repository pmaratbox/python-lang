# 0664 — Nested dependency chain

Uses **dependency-injector** (`DeclarativeContainer` with `providers.Singleton`)
to register a 3-level dependency chain `A -> B -> C`. Each `Singleton` provider
is wired to the one below it (`b=a`, `c=b`), so resolving `container.c()` builds
the whole graph: `C` receives `B`, which receives `A`. Calling `c.v()` walks the
chain — `A.v()` returns `a`, `B` appends `b`, `C` appends `c` — yielding `abc`,
which comes entirely from resolving through the container.

## Run

    python3 main.py
