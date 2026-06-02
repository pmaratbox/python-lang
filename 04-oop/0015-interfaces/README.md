# 0015 — Interfaces

Define a `Shape` interface with `name()` and `area()` methods, implement it for a rectangle and a square, then loop over a collection of shapes and print each one's area. Python expresses an interface as an *abstract base class*: `Shape(ABC)` whose `@abstractmethod` members each subclass must override. Paired with `@dataclass`, every shape carries its own fields and supplies its own `name()`/`area()`. Iterating a `list[Shape]` and calling `s.area()` dispatches to the concrete type at runtime — and because Python is duck-typed, the ABC documents and enforces the contract rather than being strictly required.

## Run

    python3 main.py
