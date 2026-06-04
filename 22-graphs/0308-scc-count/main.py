import sys


def main():
    n = 4
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for u, v in [(0, 1), (1, 2), (2, 0), (2, 3)]:
        adj[u].append(v)
        radj[v].append(u)

    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * n

    def dfs2(u, c):
        comp[u] = c
        for v in radj[u]:
            if comp[v] == -1:
                dfs2(v, c)

    count = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, count)
            count += 1
    print(count)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
