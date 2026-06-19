# httpx client + WSGITransport (in-process, NO socket/port). Run: python3 main.py
import httpx

def app(environ, start_response):
    # The server defines NO routes, so every request falls through to 404.
    start_response("404 Not Found", [])
    return [b""]

c = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
print(c.get("/missing").status_code)  # 404
