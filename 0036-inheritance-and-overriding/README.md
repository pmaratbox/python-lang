# 0036 — Inheritance & Overriding

Define a base `Animal` with a `speak` method, a `Dog` that overrides it, and call both, printing `animal: some sound` and `dog: Woof`. A subclass lists its parent in parentheses (`class Dog(Animal)`) and redefines `speak` to override it. Method lookup walks the MRO (method resolution order), and `super().speak()` would reach the parent's version.

## Run

    python3 main.py
