# 0107 — Worker Pool

Distribute squaring of 1..4 across a pool of workers, collect the results, and print them sorted ascending `1 4 9 16`. `concurrent.futures.ThreadPoolExecutor` is the standard worker pool, and the results are sorted before printing.

## Run

    python3 main.py
