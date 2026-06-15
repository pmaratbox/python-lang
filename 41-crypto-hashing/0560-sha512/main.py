import hashlib

digest = hashlib.sha512(b"hello").hexdigest()
print(digest)
