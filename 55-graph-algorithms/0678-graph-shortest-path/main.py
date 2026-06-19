import networkx as nx

# Fixed weighted undirected graph G.
G = nx.Graph()
G.add_weighted_edges_from([
    ("a", "b", 1),
    ("a", "c", 4),
    ("b", "c", 1),
    ("b", "d", 5),
    ("c", "d", 1),
    ("d", "e", 1),
])

# Unique weighted shortest path a -> e, joined with '-'.
path = nx.shortest_path(G, "a", "e", weight="weight")
print("-".join(path))
