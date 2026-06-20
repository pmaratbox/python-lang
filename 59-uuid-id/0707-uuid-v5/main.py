import uuid

# UUIDv5 is name-based: it hashes (namespace, name) with SHA-1, so the
# same inputs always yield the same UUID. This is deterministic, unlike
# the random UUIDv4.
print(uuid.uuid5(uuid.NAMESPACE_DNS, "example.com"))
