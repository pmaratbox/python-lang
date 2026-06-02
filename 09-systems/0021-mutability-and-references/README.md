# 0021 — Mutability & References

Have a function increment a value in place — through a pointer, reference, or mutable holder — so the caller sees it change from `before: 1` to `after: 2`. Python passes object references by value, but `int` is immutable, so rebinding inside a function would not escape. To mutate visibly the caller passes a *mutable* object — here a one-element `list` — and the function updates its contents with `box[0] += 1`.

## Run

    python3 main.py
