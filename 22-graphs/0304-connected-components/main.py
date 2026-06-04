def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def main():
    n = 5
    parent = list(range(n))
    for u, v in [(0, 1), (1, 2), (3, 4)]:
        parent[find(parent, u)] = find(parent, v)
    roots = {find(parent, i) for i in range(n)}
    print(len(roots))


if __name__ == "__main__":
    main()
