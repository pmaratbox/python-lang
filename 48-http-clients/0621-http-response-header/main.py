# httpx client + WSGITransport (in-process, NO socket/port). Run: python3 main.py
import httpx


def app(environ, start_response):
    if environ["PATH_INFO"] == "/info":
        start_response("200 OK", [("X-Count", "7")])
        return [b""]
    start_response("404 Not Found", [])
    return [b""]


client = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
resp = client.get("/info")
print(resp.headers["X-Count"])
