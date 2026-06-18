import yaml

doc = "server:\n  host: localhost\n  port: 8080\n"
data = yaml.safe_load(doc)
server = data["server"]
print(f"{server['host']}:{server['port']}")
