# 0677 — Shortest distance

Python's `networkx` library builds the weighted undirected graph G and computes the weighted shortest-path distance from `a` to `e` with `nx.shortest_path_length(..., weight="weight")`, which runs Dijkstra's algorithm. The unique shortest route `a-b-c-d-e` has total cost `4`.

## Run

    python3 main.py
