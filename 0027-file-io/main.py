import os

path = "greeting.txt"
with open(path, "w") as f:
    f.write("hello, file")

with open(path) as f:
    content = f.read()

os.remove(path)
print(f"read: {content}")
