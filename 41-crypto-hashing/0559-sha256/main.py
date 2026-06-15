import hashlib

# Compute the SHA-256 of the UTF-8 bytes of "hello" and print the lowercase hex digest.
digest = hashlib.sha256("hello".encode("utf-8")).hexdigest()
print(digest)
