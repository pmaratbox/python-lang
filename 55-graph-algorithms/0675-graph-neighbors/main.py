import networkx as nx

G = nx.Graph()
G.add_weighted_edges_from(
    [("a", "b", 1), ("a", "c", 4), ("b", "c", 1), ("b", "d", 5), ("c", "d", 1), ("d", "e", 1)]
)

print(",".join(sorted(G.neighbors("a"))))
