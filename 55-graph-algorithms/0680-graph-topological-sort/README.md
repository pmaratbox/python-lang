# 0680 — Topological sort

Using the `networkx` graph library, we build a directed acyclic graph (`DiGraph`) with edges `a->b`, `b->c`, `a->c`, `c->d`, `d->e` and call `nx.topological_sort`, which returns a linear ordering of the nodes such that every edge points from an earlier node to a later one. For this DAG the order is unique: `a,b,c,d,e`.

## Run

    python3 main.py
