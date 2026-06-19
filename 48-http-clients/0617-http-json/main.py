# httpx client + WSGITransport (in-process, NO socket/port). Run: python3 main.py
import httpx, json


def app(environ, start_response):
    if environ["PATH_INFO"] == "/user":
        start_response("200 OK", [("Content-Type", "application/json")])
        return [json.dumps({"name": "Alice", "age": 30}).encode()]
    start_response("404 Not Found", [])
    return [b""]


c = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
print(c.get("/user").json()["name"])
