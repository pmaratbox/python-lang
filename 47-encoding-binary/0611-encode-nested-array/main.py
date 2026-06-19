import msgpack

print(msgpack.packb([[1, 2], [3, 4]], use_bin_type=True).hex())
