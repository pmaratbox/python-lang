import csv, io

data = "name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,35,Berlin\n"

rows = list(csv.DictReader(io.StringIO(data)))  # parse with header names
ages = [r["age"] for r in rows]                 # pull the `age` column by name
print(",".join(ages))
