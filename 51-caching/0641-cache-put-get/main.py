from cachetools import LRUCache

c = LRUCache(maxsize=3)
c["a"] = 1                    # put
print(c.get("a", "miss"))     # get the stored value (prints 1)
