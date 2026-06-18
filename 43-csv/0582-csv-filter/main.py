import csv, io

data = "name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,35,Berlin\n"

rows = list(csv.DictReader(io.StringIO(data)))      # parse by header name
kept = [r["name"] for r in rows if int(r["age"]) > 28]  # Alice 30, Carol 35
print(",".join(kept))
