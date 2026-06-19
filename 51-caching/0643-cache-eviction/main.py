from cachetools import LRUCache

cache = LRUCache(maxsize=3)
# No gets between puts, so order is purely by insertion: a is least-recent.
for key, value in [("a", 1), ("b", 2), ("c", 3), ("d", 4)]:
    cache[key] = value

# Inserting d=4 over capacity evicted the least-recently-used key, a.
print(cache.get("a", "miss"), cache.get("d", "miss"))
