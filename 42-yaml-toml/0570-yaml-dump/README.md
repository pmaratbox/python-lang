# 0570 — Dump YAML

Serialize a fixed map (`name=Alice`, `age=30`, `city=Paris`) to YAML using PyYAML's `yaml.dump`. With `sort_keys=True` the keys come out alphabetically and `default_flow_style=False` selects block style (no flow braces, no quotes on these simple scalars), producing output verified byte-identical across PyYAML, js-yaml, serde_yaml, SnakeYAML, YamlDotNet, and go yaml.v3.

## Run

    python3 main.py
