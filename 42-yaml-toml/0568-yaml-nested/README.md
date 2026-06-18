# 0568 — Nested YAML mapping

Parse a small YAML document with a nested `server` mapping using PyYAML's `yaml.safe_load`, then read the nested `server.host` and `server.port` values and print them joined as `host:port`. PyYAML returns nested mappings as plain Python dicts, so the inner values are reached by ordinary key lookups.

## Run

    python3 main.py
