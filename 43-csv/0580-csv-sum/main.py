import csv, io

data = "name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,35,Berlin\n"

rows = list(csv.DictReader(io.StringIO(data)))  # parse by header name
total = sum(int(r["age"]) for r in rows)        # 30 + 25 + 35
print(total)
