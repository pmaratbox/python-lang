# httpx client + WSGITransport (in-process, NO socket/port). Run: python3 main.py
import httpx


def app(environ, start_response):
    if environ["PATH_INFO"] == "/item" and environ["REQUEST_METHOD"] == "PUT":
        start_response("200 OK", [])
        return [b"updated"]
    start_response("404 Not Found", [])
    return [b""]


client = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
resp = client.put("/item")
print(resp.text)
