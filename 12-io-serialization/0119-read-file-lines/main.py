import os

path = "filelines.txt"
with open(path, "w") as f:
    f.write("one\n")
    f.write("two\n")
    f.write("three\n")

with open(path) as f:
    lines = [line for line in f if line.strip()]

os.remove(path)
print("lines:", len(lines))
