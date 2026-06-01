# 0035 — Ranges & Slicing

From the list `[10, 20, 30, 40, 50]`, take the sub-sequence at indices 1 through 4 (exclusive) and print `slice: 20 30 40`. Slice syntax `nums[1:4]` is half-open — it includes index 1 up to but not including 4 — and returns a new list. Omitting bounds (`nums[:3]`, `nums[2:]`) or adding a step (`nums[::2]`) extends it; negative indices count from the end.

## Run

    python3 main.py
