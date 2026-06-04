def bellman_ford(edges, src, n):
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


def main():
    n = 3
    edges = [(0, 1, 1), (1, 2, -2), (0, 2, 4)]
    dist = bellman_ford(edges, 0, n)
    print(" ".join(str(d) for d in dist))


if __name__ == "__main__":
    main()
