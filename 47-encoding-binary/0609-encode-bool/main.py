import msgpack

print(msgpack.packb(True, use_bin_type=True).hex())
