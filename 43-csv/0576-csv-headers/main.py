import csv, io

data = "name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,35,Berlin\n"

rows = list(csv.reader(io.StringIO(data)))  # rows[0] is the header row
print("|".join(rows[0]))                    # join the header fields with a pipe
