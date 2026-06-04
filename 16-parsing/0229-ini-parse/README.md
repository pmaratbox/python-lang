# 0229 — Parse INI

Parse the INI text with section [s] and key k=v, printing the flattened entry `s.k=v`. `str.split("=", 1)` cleanly separates the key from a value that might itself contain "=".

## Run

    python3 main.py
