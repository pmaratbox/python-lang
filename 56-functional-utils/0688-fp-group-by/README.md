# 0688 — Group by

Python's `toolz` library groups `[1..6]` by parity with `toolz.groupby`, which maps each element through a key function (`even`/`odd`) into a dict of lists, then prints the groups with keys sorted as `key:v1,v2,...` joined by `;`, producing `even:2,4,6;odd:1,3,5`.

## Run

    python3 main.py
