import csv, io

data = 'name,note\nAlice,"hello, world"\n'

rows = list(csv.reader(io.StringIO(data)))  # rows[0] is the header
note = rows[1][1]                           # quoted field keeps its comma
print(note)
