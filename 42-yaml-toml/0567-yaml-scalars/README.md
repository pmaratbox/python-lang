# 0567 — YAML scalars

Parse a small YAML mapping with PyYAML's `yaml.safe_load` and read three scalar fields. The document `name: Alice\nrole: admin\nage: 30\n` becomes a Python dict; `age` is parsed as the integer `30`. The three values are printed space-joined.

## Run

    python3 main.py
