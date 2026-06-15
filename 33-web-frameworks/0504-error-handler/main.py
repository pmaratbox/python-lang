import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/boom")
def boom():
    raise RuntimeError("kaboom")


# raise_server_exceptions=False lets the framework's own error handling
# turn the thrown error into a real 500 response instead of re-raising it.
client = TestClient(app, raise_server_exceptions=False)
r = client.get("/boom")
print(r.status_code)
