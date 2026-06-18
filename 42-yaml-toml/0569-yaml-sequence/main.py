import yaml

doc = "fruits:\n  - apple\n  - banana\n  - cherry\n"
data = yaml.safe_load(doc)
print(",".join(data["fruits"]))
