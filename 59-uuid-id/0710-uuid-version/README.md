# 0710 — UUID version

Uses Python's stdlib [`uuid`](https://docs.python.org/3/library/uuid.html) library to parse the UUID string `550e8400-e29b-41d4-a716-446655440000` into a `uuid.UUID` object. The `.version` attribute reports which UUID version the value encodes (the 4 high bits of the 7th byte). For this value the version is `4`, so we print `4`.

## Run

    python3 main.py
