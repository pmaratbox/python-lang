import networkx as nx

D = nx.DiGraph([("a", "b"), ("b", "c"), ("a", "c"), ("c", "d"), ("d", "e")])
print(",".join(nx.topological_sort(D)))
