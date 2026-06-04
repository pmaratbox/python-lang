WHITE, GRAY, BLACK = 0, 1, 2


def has_cycle(adj, n):
    color = [WHITE] * n

    def dfs(u):
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False

    return any(color[u] == WHITE and dfs(u) for u in range(n))


def main():
    n = 3
    adj = [[] for _ in range(n)]
    for u, v in [(0, 1), (1, 2), (2, 0)]:
        adj[u].append(v)
    print("cycle" if has_cycle(adj, n) else "acyclic")


if __name__ == "__main__":
    main()
