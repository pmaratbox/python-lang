import msgpack

print(msgpack.packb(42, use_bin_type=True).hex())
