# 0608 — Encode a string

Uses Python's `msgpack` library to MessagePack-encode the string `"hello"` and print the lowercase hex of the resulting bytes (`a5` fixstr header + the 5 UTF-8 bytes of `hello`).

## Run

    python3 main.py
