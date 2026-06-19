# 0612 — Encode a map

Using the real `msgpack` library, MessagePack-encode the single-key map `{"a": 1}` and print the lowercase hex of the resulting bytes: a fixmap header (`81`), the key `"a"` (`a161`), and the value `1` (`01`).

## Run

    python3 main.py
