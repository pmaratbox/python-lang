class Dfs:
    def __init__(self, adj):
        self.adj = adj
        self.visited = set()
        self.order = []

    def traverse(self, node):
        self.visited.add(node)
        self.order.append(node)
        for neighbor in self.adj[node]:
            if neighbor not in self.visited:
                self.traverse(neighbor)
        return self.order


def main():
    adj = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    dfs = Dfs(adj)
    print(" ".join(str(n) for n in dfs.traverse(0)))


if __name__ == "__main__":
    main()
