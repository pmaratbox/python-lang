from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/users/{id}", response_class=PlainTextResponse)
def get_user(id: str):
    return id


client = TestClient(app)
print(client.get("/users/42").text)
