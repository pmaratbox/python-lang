from cachetools import LRUCache

# Capacity-3 strict LRU cache.
cache = LRUCache(maxsize=3)
cache["a"] = 1
cache["b"] = 2
cache["c"] = 3

# A get promotes "a" to most-recently-used, so "b" becomes the LRU.
_ = cache["a"]

# Inserting "d" overflows capacity and evicts the LRU key ("b").
cache["d"] = 4

# "a" survived (promoted); "b" was evicted -> "miss".
print(cache.get("a", "miss"), cache.get("b", "miss"))
