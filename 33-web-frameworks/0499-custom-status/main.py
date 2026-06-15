import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.post("/create", status_code=201)
def create():
    return {"created": True}


client = TestClient(app)
r = client.post("/create")
print(r.status_code)
