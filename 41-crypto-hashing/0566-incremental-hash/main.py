import hashlib

h = hashlib.sha256()
h.update(b"foo")
h.update(b"bar")
print(h.hexdigest())
