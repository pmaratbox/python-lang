import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/item", response_class=PlainTextResponse)
def get_item():
    return "get"


@app.post("/item", response_class=PlainTextResponse)
def post_item():
    return "post"


client = TestClient(app)
response = client.post("/item")
print(response.text)
