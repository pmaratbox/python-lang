import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()


class Pair(BaseModel):
    a: int
    b: int


@app.post("/sum", response_class=PlainTextResponse)
def add(pair: Pair):
    return str(pair.a + pair.b)


client = TestClient(app)
r = client.post("/sum", json={"a": 2, "b": 3})
print(r.text)
