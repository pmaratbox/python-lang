import uuid

# UUIDv5 (name-based, SHA-1) is deterministic: same namespace + name -> same UUID.
a = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
b = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print(str(a == b).lower())
