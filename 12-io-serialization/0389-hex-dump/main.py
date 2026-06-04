data = "Hi".encode("utf-8")
print(" ".join("{:02x}".format(b) for b in data))
