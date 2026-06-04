import json

obj = {"name": "Ada", "age": 36}
print(json.dumps(obj, separators=(",", ":")))
