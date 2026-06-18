import tomllib

# Parse a TOML array-of-tables ([[servers]]) with the stdlib tomllib parser,
# then collect each server's name and join them with commas.
doc = tomllib.loads('[[servers]]\nname = "alpha"\n[[servers]]\nname = "beta"\n')
print(",".join(s["name"] for s in doc["servers"]))
