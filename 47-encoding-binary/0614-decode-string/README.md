# 0614 — Decode bytes

Uses Python's `msgpack` library to DECODE the fixed MessagePack hex string `a568656c6c6f` back into a value: the hex is converted to bytes with `bytes.fromhex` and decoded via `msgpack.unpackb(..., raw=False)`, yielding the string `hello`.

## Run

    python3 main.py
