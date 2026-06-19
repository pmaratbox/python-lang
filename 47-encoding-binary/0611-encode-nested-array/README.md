# 0611 — Encode a nested array

Uses the real `msgpack` library to MessagePack-encode the nested array `[[1, 2], [3, 4]]` and print the lowercase hex of the resulting bytes (`92` fixarray-of-2, each element itself a `92` fixarray of two positive fixints).

## Run

    python3 main.py
