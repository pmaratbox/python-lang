# 0424 — Signal + Computed

Implement fine-grained reactivity: a writable signal and a derived computed that recomputes when its dependency changes. A callable `Signal` object holds subscribers and the `Computed` registers its recompute method as a subscriber.

## Run

    python3 main.py
