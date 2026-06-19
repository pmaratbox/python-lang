import httpx


def app(environ, start_response):
    if environ["PATH_INFO"] == "/token":
        start_response("200 OK", [])
        return [environ.get("HTTP_X_TOKEN", "").encode()]
    start_response("404 Not Found", [])
    return [b""]


c = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
print(c.get("/token", headers={"X-Token": "secret"}).text)
