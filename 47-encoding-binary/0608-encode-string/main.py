import msgpack

value = "hello"
encoded = msgpack.packb(value, use_bin_type=True)
print(encoded.hex())
