import uuid

# UUIDv5 is name-based (SHA-1) and DETERMINISTIC: the same (namespace, name)
# always yields the same UUID. Here we hash the DNS-namespaced name "test.com".
# A different name than "example.com" produces a different UUID.
print(uuid.uuid5(uuid.NAMESPACE_DNS, "test.com"))
