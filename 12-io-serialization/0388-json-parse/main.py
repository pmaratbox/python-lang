import json

data = json.loads('{"x":1,"y":2}')
print(" ".join("{}={}".format(k, v) for k, v in data.items()))
