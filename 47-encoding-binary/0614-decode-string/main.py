import msgpack

hex_str = "a568656c6c6f"
value = msgpack.unpackb(bytes.fromhex(hex_str), raw=False)
print(value)
