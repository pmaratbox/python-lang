import heapq


def main():
    n = 4
    adj = [[] for _ in range(n)]
    for u, v, w in [(0, 1, 1), (1, 2, 2), (2, 3, 3)]:
        adj[u].append((v, w))
        adj[v].append((u, w))
    visited = [False] * n
    pq = [(0, 0)]
    total = 0
    while pq:
        w, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        for v, ww in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (ww, v))
    print(total)


if __name__ == "__main__":
    main()
