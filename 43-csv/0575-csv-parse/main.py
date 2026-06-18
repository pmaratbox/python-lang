import csv, io

data = "name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,35,Berlin\n"

rows = list(csv.reader(io.StringIO(data)))  # rows[0] is the header row
names = [r[0] for r in rows[1:]]            # first column of each data row
print(",".join(names))
