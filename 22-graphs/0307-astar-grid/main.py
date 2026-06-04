import heapq


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    size = 3
    start, goal = (0, 0), (2, 2)
    g = {start: 0}
    pq = [(manhattan(start, goal), start)]
    while pq:
        _, cur = heapq.heappop(pq)
        if cur == goal:
            print(g[cur])
            return
        r, c = cur
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size:
                ng = g[cur] + 1
                nxt = (nr, nc)
                if ng < g.get(nxt, float("inf")):
                    g[nxt] = ng
                    heapq.heappush(pq, (ng + manhattan(nxt, goal), nxt))


if __name__ == "__main__":
    main()
