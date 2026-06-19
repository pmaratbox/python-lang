# 0660 — Bind interface to impl

Use the `dependency-injector` container to bind the abstract `Animal` interface to a concrete `Dog` implementation. The container resolves the binding when we request `animal`, and calling `sound()` on the resolved instance prints `woof`.

## Run

    python3 main.py
