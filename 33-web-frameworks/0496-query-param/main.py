import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/greet", response_class=PlainTextResponse)
def greet(name: str):
    return "hello " + name


client = TestClient(app)
response = client.get("/greet", params={"name": "alice"})
print(response.text)
