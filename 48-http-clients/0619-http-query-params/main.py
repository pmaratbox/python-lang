# httpx client + WSGITransport (in-process, NO socket/port).
from urllib.parse import parse_qs

import httpx


def app(environ, start_response):
    path = environ["PATH_INFO"]
    qs = parse_qs(environ.get("QUERY_STRING", ""))
    if path == "/greet":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [f"hi {qs['name'][0]}".encode()]
    start_response("404 Not Found", [])
    return [b""]


client = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
print(client.get("/greet", params={"name": "Bob"}).text)
