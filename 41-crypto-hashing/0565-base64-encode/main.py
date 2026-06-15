import base64

# Base64-encode the UTF-8 bytes of "hello" using the stdlib base64 module.
encoded = base64.b64encode(b"hello").decode()
print(encoded)
