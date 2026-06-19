import msgpack

print(msgpack.packb([1, 2, 3], use_bin_type=True).hex())
