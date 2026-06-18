import tomllib

doc = '[server]\nhost = "localhost"\nport = 8080\n'
t = tomllib.loads(doc)
server = t["server"]
print(f"host={server['host']} port={server['port']}")
