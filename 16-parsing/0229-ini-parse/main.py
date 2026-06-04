def parse_ini(text):
    section = ""
    entries = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1]
        elif "=" in line:
            key, value = line.split("=", 1)
            entries.append("{}.{}={}".format(section, key.strip(), value.strip()))
    return entries


text = "[s]\nk=v\n"
for entry in parse_ini(text):
    print(entry)
