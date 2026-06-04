def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def main():
    n = 3
    parent = list(range(n))
    edges = sorted([(0, 1, 1), (1, 2, 2), (0, 2, 3)], key=lambda e: e[2])
    total = 0
    for u, v, w in edges:
        ru, rv = find(parent, u), find(parent, v)
        if ru != rv:
            parent[ru] = rv
            total += w
    print(total)


if __name__ == "__main__":
    main()
