# 0106 — Producer / Consumer

A producer sends 1..5 to a consumer that sums them, printing `15`. A bounded `queue.Queue(maxsize=2)` applies backpressure between the two threads.

## Run

    python3 main.py
