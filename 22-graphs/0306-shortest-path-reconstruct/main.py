import heapq


def main():
    n = 4
    adj = [[] for _ in range(n)]
    for u, v, w in [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]:
        adj[u].append((v, w))
    dist = [float("inf")] * n
    prev = [-1] * n
    dist[0] = 0
    pq = [(0, 0)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    path = []
    cur = 3
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    print(" ".join(str(x) for x in path))


if __name__ == "__main__":
    main()
