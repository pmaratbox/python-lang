# 0073 — Caesar Cipher

Encrypt `abc` with a Caesar cipher shifting each letter forward by `1` (wrapping within the alphabet) and print the result: `bcd`. Each letter is mapped to `0..25` via `ord(ch) - ord('a')`, shifted modulo 26, and mapped back with `chr` — so `z` would wrap to `a`.

## Run

    python3 main.py
