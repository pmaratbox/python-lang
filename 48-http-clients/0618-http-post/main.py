# httpx client + WSGITransport (in-process, NO socket/port). Run: python3 main.py
import httpx


def app(environ, start_response):
    if environ["PATH_INFO"] == "/echo" and environ["REQUEST_METHOD"] == "POST":
        n = int(environ.get("CONTENT_LENGTH") or 0)
        body = environ["wsgi.input"].read(n)
        start_response("200 OK", [])
        return [body]
    start_response("404 Not Found", [])
    return [b""]


client = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
resp = client.post("/echo", content=b"ping")
print(resp.text)
