# 0391 — URL Percent-Encode

Percent-encode the string "a b&c" to `a%20b%26c`. `urllib.parse.quote` with `safe=""` percent-encodes reserved chars using uppercase hex.

## Run

    python3 main.py
