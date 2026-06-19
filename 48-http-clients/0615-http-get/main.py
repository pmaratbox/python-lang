# httpx client + WSGITransport (in-process, NO socket/port). Run: python3 main.py
import httpx


def app(environ, start_response):
    if environ["PATH_INFO"] == "/hello":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"hello world"]
    start_response("404 Not Found", [])
    return [b""]


c = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
print(c.get("/hello").text)
