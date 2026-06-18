import tomllib

# Parse a fixed TOML document with two top-level keys using the stdlib tomllib parser.
doc = 'title = "demo"\nversion = 2\n'
t = tomllib.loads(doc)

# title is a string, version is an integer; print them space-joined.
print(f"{t['title']} {t['version']}")
