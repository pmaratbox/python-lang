def parse_row(row):
    fields = []
    current = []
    in_quotes = False
    for c in row:
        if c == '"':
            in_quotes = not in_quotes
        elif c == "," and not in_quotes:
            fields.append("".join(current))
            current = []
        else:
            current.append(c)
    fields.append("".join(current))
    return fields


print("|".join(parse_row('a,"b,c",d')))
