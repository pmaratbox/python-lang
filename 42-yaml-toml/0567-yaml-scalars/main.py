import yaml

doc = "name: Alice\nrole: admin\nage: 30\n"
d = yaml.safe_load(doc)
print(f"{d['name']} {d['role']} {d['age']}")
