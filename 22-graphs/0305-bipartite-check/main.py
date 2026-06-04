from collections import deque


def is_bipartite(adj, n):
    color = [-1] * n
    for s in range(n):
        if color[s] != -1:
            continue
        color[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True


def build(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def main():
    square = build(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    triangle = build(3, [(0, 1), (1, 2), (2, 0)])
    a = "yes" if is_bipartite(square, 4) else "no"
    b = "yes" if is_bipartite(triangle, 3) else "no"
    print(a, b)


if __name__ == "__main__":
    main()
