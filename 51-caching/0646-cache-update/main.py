from cachetools import LRUCache

cache = LRUCache(maxsize=3)
cache["a"] = 1
cache["a"] = 2  # re-putting the same key replaces its value, not a new entry

# Reading the key back returns the most recently stored value.
print(cache.get("a", "miss"))
