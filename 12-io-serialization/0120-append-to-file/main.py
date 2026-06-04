import os

path = "tofile.txt"
with open(path, "w") as f:
    f.write("a\n")
with open(path, "a") as f:
    f.write("b\n")

with open(path) as f:
    lines = [line.strip() for line in f if line.strip()]

os.remove(path)
print(" ".join(lines))
