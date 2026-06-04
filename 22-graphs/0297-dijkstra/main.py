import heapq


def dijkstra(adj, src, n):
    dist = [float("inf")] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def main():
    n = 4
    adj = [[] for _ in range(n)]
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
    for u, v, w in edges:
        adj[u].append((v, w))
    dist = dijkstra(adj, 0, n)
    print(" ".join(str(d) for d in dist))


if __name__ == "__main__":
    main()
