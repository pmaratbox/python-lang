# 0607 — Encode an integer

Uses the real `msgpack` library to MessagePack-encode the integer `42` and print the lowercase hex of the resulting bytes. Small non-negative integers serialize as a single positive fixint byte, so `42` becomes `2a`.

## Run

    python3 main.py
