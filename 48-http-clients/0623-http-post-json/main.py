import httpx, json


def app(environ, start_response):
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]
    if path == "/double" and method == "POST":
        n = int(environ.get("CONTENT_LENGTH") or 0)
        x = json.loads(environ["wsgi.input"].read(n))["x"]
        start_response("200 OK", [("Content-Type", "application/json")])
        return [json.dumps({"doubled": x * 2}).encode()]
    start_response("404 Not Found", [])
    return [b""]


c = httpx.Client(transport=httpx.WSGITransport(app=app), base_url="http://test")
print(c.post("/double", json={"x": 5}).json()["doubled"])
