import yaml

m = {"name": "Alice", "age": 30, "city": "Paris"}
print(yaml.dump(m, sort_keys=True, default_flow_style=False), end="")
