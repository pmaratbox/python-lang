# 0708 — UUIDv5 is stable

Using Python's standard-library `uuid` module, this program generates a name-based
UUIDv5 (SHA-1) from the DNS namespace and the name `example.com` twice, then prints
whether the two results are equal. Because UUIDv5 is deterministic from its
`(namespace, name)` pair, the answer is always `true`.

## Run

    python3 main.py
