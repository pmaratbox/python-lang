import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/user")
def user():
    return {"name": "alice"}


client = TestClient(app)
r = client.get("/user")
print(r.text)
