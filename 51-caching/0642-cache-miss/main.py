from cachetools import LRUCache

# cachetools.LRUCache is Python's strict-LRU cache (capacity = maxsize).
c = LRUCache(maxsize=3)

# Look up `x` in an empty cache. get(key, default) returns the default
# when the key is absent rather than raising KeyError.
print(c.get("x", "miss"))  # miss (key never put)
