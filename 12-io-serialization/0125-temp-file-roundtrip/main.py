import os
import tempfile

text = "ok-data"
fd, path = tempfile.mkstemp()
with os.fdopen(fd, "w") as f:
    f.write(text)

with open(path) as f:
    read_back = f.read()

os.remove(path)
print("roundtrip:", "ok" if read_back == text else "fail")
