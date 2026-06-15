import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def home():
    return "home"


@app.get("/about", response_class=PlainTextResponse)
def about():
    return "about"


client = TestClient(app)
print(client.get("/").text)
print(client.get("/about").text)
