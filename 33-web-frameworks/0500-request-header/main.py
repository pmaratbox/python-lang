import logging

logging.disable(logging.CRITICAL)

from fastapi import FastAPI, Header
from fastapi.responses import PlainTextResponse
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/whoami", response_class=PlainTextResponse)
def whoami(x_name: str = Header()):
    return x_name


client = TestClient(app)
response = client.get("/whoami", headers={"X-Name": "alice"})
print(response.text)
