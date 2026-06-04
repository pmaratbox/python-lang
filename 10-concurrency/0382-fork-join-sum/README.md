# 0382 — Fork-Join Sum

Recursively fork the sum of [1..8] into halves and join the partial sums, printing `36`. Each half is submitted to a thread pool and joined via `Future.result()`.

## Run

    python3 main.py
