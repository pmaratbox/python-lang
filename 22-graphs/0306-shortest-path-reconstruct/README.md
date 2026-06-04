# 0306 — Reconstruct Shortest Path

On the Dijkstra graph 0->1(4),0->2(1),2->1(2),1->3(1),2->3(5), print the actual shortest path from 0 to 3 `0 2 1 3`. A `prev` array recorded during relaxation lets us backtrack and `reverse` the path.

## Run

    python3 main.py
