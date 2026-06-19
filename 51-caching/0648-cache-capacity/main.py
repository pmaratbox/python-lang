from cachetools import LRUCache

cache = LRUCache(maxsize=3)
for key, value in [("a", 1), ("b", 2), ("c", 3), ("d", 4)]:
    cache[key] = value

# Four items were inserted, but the LRU cache never grows past its capacity.
print(len(cache))
