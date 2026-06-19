from cachetools import LRUCache

cache = LRUCache(maxsize=5)
cache["a"] = 1
cache["b"] = 2

# Two entries inserted under a capacity of 5 (no eviction), so len() is 2.
print(len(cache))
