import heapq

data = [3, 1, 4, 1, 5]
# Build a max-heap by negating values.
heap = [-x for x in data]
heapq.heapify(heap)

out = [-heapq.heappop(heap) for _ in range(3)]
print(" ".join(str(x) for x in out))
