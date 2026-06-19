import msgpack

print(msgpack.packb(None, use_bin_type=True).hex())
