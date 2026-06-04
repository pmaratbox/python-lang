# 0172 — Ring Buffer

Push 1,2,3,4,5 into a fixed capacity-3 ring buffer (overwriting oldest) and print the final contents `3 4 5`. A circular buffer tracks a `start` index and `size`, advancing `start` modulo capacity once full.

## Run

    python3 main.py
