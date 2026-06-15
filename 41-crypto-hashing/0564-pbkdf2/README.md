# 0564 — PBKDF2

Derives a 32-byte key from the password `password` and salt `salt` using the standard library's `hashlib.pbkdf2_hmac`, running PBKDF2 with HMAC-SHA256 for 1000 iterations. The derived key is printed as lowercase hex.

## Run

    python3 main.py
