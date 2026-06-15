import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.testclient import TestClient

app = FastAPI()


@app.middleware("http")
async def prefix_body(request: Request, call_next):
    response = await call_next(request)
    body = b"".join([chunk async for chunk in response.body_iterator])
    new_body = b"[mw] " + body
    return PlainTextResponse(new_body, status_code=response.status_code)


@app.get("/", response_class=PlainTextResponse)
def root():
    return "hello"


client = TestClient(app)
response = client.get("/")
print(response.text)
