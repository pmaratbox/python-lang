# 0663 — Factory provider

Build a service via a factory. A `providers.Factory` in the `dependency-injector` container is wired to a factory function `build_widget`, which constructs a `Widget`. Resolving `container.widget()` runs the factory through the container and the resolved object's `value()` returns `built`.

## Run

    python3 main.py
