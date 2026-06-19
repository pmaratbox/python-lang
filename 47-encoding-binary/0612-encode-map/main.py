import msgpack

print(msgpack.packb({"a": 1}, use_bin_type=True).hex())
