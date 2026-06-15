# 0566 — Incremental hashing

The standard-library `hashlib` module lets you feed data into a hash in stages: create a SHA-256 hasher with `hashlib.sha256()`, call `.update(b"foo")` then `.update(b"bar")` to absorb the bytes incrementally, and `.hexdigest()` to finalize. The result is identical to hashing the concatenated input `b"foobar"` in one shot, printed as a lowercase hex string.

## Run

    python3 main.py
