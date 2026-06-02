# 0010 — Structs

Define a `Person` type with a `name` and an `age`, create one ("Ada", 36), and
print each field. A `@dataclass` turns a class with typed field annotations into
a record — it auto-generates `__init__`, `__repr__`, and equality. Fields are
read with dot access (`p.name`). Plain classes and `NamedTuple` are
alternatives.

## Run

    python3 main.py
