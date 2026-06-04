import base64

encoded = base64.b64encode(b"hi").decode("ascii")
print(encoded)
