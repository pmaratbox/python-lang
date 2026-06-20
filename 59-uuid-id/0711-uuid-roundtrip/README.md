# 0711 — Parse and format

Uses Python's stdlib `uuid` library to parse an UPPERCASE UUID string and round-trip it back to text. `uuid.UUID("550E8400-E29B-41D4-A716-446655440000")` parses the hex (case-insensitively, ignoring the dashes), and `str(...)` formats it back in the canonical lowercase, hyphenated form. The program prints the canonical lowercase UUID.

## Run

    python3 main.py
