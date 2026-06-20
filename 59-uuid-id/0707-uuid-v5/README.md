# 0707 — UUIDv5 (name-based)

Uses Python's stdlib `uuid` library to generate a name-based UUIDv5 with `uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")`. UUIDv5 hashes the namespace plus name with SHA-1, so it is fully deterministic: the same `(namespace, name)` pair always produces the same UUID (unlike the random UUIDv4). Using the standard DNS namespace `6ba7b810-9dad-11d1-80b4-00c04fd430c8` with the name `example.com` always yields `cfbff0d1-9375-5685-968c-48ce8b15ae17`.

## Run

    python3 main.py
