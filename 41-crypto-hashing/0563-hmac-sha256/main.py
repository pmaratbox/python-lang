import hashlib
import hmac

digest = hmac.new(b"key", b"hello", hashlib.sha256).hexdigest()
print(digest)
