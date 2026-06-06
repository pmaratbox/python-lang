# 0423 — EventEmitter (Pub/Sub)

Build a multi-topic EventEmitter with on(topic, handler), emit(topic, payload), and off(topic, handler). A dict maps each topic to a list of handler callables, and emit iterates a copy so off during dispatch stays safe.

## Run

    python3 main.py
