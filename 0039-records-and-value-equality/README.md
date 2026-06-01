# 0039 — Records & Value Equality

Create two points with the same fields, print one as `point: (1, 2)`, and compare them by value to print `equal: yes`. `@dataclass(frozen=True)` generates `__init__`, `__repr__`, and a field-wise `__eq__`, and makes instances immutable (and hashable). So two points with equal fields compare equal with `==`.

## Run

    python3 main.py
