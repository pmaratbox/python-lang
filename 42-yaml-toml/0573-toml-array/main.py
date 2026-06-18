import tomllib

doc = 'tags = ["red", "green", "blue"]\n'
data = tomllib.loads(doc)
print(",".join(data["tags"]))
