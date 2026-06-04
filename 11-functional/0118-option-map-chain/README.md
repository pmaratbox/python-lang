# 0118 — Option Map Chaining

Map a function over a present optional (10 -> 12) and an absent one (-> fallback), printing `12 none`. Python uses `None` for absence, so mapping short-circuits when the value is `None`.

## Run

    python3 main.py
