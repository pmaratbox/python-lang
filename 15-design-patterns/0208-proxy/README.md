# 0208 — Virtual Proxy

Use a lazy virtual proxy that loads the real subject only on first access, printing `loaded`. The proxy holds `None` until the first request, then instantiates the real subject.

## Run

    python3 main.py
