from cachetools import LRUCache

cache = LRUCache(maxsize=3)
cache["a"] = 1

# Membership tests with `in` do not promote recency in cachetools.
has_a = "a" in cache
has_x = "x" in cache

# Booleans print lowercase when formatted as strings.
print(str(has_a).lower(), str(has_x).lower())
