# 0105 — Channels / Message Passing

Send the values 1, 2, 3 through a channel (or queue) from one thread and receive them in order, printing `1 2 3`. A `queue.Queue` is Python's thread-safe channel, with a `None` sentinel signalling close.

## Run

    python3 main.py
