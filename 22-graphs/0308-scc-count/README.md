# 0308 — Strongly Connected Components

Count the strongly connected components of 0->1,1->2,2->0,2->3, printing `2`. Kosaraju runs one DFS for finish order, then DFS on the reversed adjacency lists.

## Run

    python3 main.py
