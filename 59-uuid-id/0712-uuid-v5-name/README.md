# 0712 — UUIDv5 of another name

Uses Python's stdlib `uuid` library to generate a version-5 (name-based, SHA-1) UUID from the standard DNS namespace and the name `test.com` via `uuid.uuid5(uuid.NAMESPACE_DNS, "test.com")`. UUIDv5 is deterministic: hashing the same `(namespace, name)` pair always returns the same UUID, so no randomness is involved. Because the result depends on the name, `test.com` yields a different UUID than `example.com`. We print the canonical lowercase string `1c39b279-6010-55d9-b677-859bffab8081`.

## Run

    python3 main.py
