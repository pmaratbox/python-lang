# 0661 — Multiple dependencies

Using the `dependency-injector` container, `Service` is wired to two dependencies, `A` and `B`, registered as `Singleton` providers. Resolving `service` builds the whole graph and `run()` returns `x()` + `y()`, printing `ab`.

## Run

    python3 main.py
