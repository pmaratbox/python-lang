import heapq

data = [3, 2, 1, 5, 6, 4]
k = 2

heap = []
for x in data:
    heapq.heappush(heap, x)
    if len(heap) > k:
        heapq.heappop(heap)

print(heap[0])
