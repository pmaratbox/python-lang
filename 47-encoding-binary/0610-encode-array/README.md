# 0610 — Encode an array

Uses Python's `msgpack` library to MessagePack-encode the integer array `[1, 2, 3]` and print the lowercase hex of the resulting bytes. The encoding is a fixarray header `93` followed by the three positive fixints `01 02 03`, giving `93010203`.

## Run

    python3 main.py
