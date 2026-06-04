import heapq


def main():
    n = 4
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 3)]:
        adj[u].append(v)
        indeg[v] += 1
    pq = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(pq)
    order = []
    while pq:
        u = heapq.heappop(pq)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(pq, v)
    print(" ".join(str(x) for x in order))


if __name__ == "__main__":
    main()
