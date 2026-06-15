import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def root():
    return "hello"


client = TestClient(app)
response = client.get("/")
print(response.text)
