pairs = [("listen", "silent"), ("hello", "world")]
for a, b in pairs:
    ana = sorted(a) == sorted(b)
    print(f"{a}/{b}: {'yes' if ana else 'no'}")
