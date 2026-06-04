# 0301 — Directed Cycle Detection

Detect a cycle in the digraph 0->1,1->2,2->0, printing `cycle`. Three-color DFS with a nested closure tracks the recursion stack via the GRAY state.

## Run

    python3 main.py
