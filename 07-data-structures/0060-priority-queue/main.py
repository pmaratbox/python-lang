import heapq

pq = []
for n in (3, 1, 2):
    heapq.heappush(pq, n)

out = []
while pq:
    out.append(str(heapq.heappop(pq)))
print(" ".join(out))
