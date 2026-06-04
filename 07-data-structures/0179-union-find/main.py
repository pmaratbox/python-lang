class Find:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)

    def connected(self, a, b):
        return self.find(a) == self.find(b)


def main():
    uf = Find(4)
    uf.union(0, 1)
    uf.union(2, 3)
    print(
        "yes" if uf.connected(0, 1) else "no",
        "yes" if uf.connected(0, 2) else "no",
    )


if __name__ == "__main__":
    main()
