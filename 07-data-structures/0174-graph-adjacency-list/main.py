class AdjacencyList:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)


def main():
    graph = AdjacencyList()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    print(" ".join(str(n) for n in graph.adj[0]))


if __name__ == "__main__":
    main()
