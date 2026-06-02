# 0045 — Abstract Classes & Methods

Define an abstract `Shape` with an abstract `area` and a concrete `describe` that uses it, then implement a `Square` of side 3 and print `area: 9`. `ABC` plus `@abstractmethod` makes `Shape` abstract — it cannot be instantiated, and a subclass must define `area`. The concrete `describe` lives in the base and calls the subclass's `area` polymorphically.

## Run

    python3 main.py
