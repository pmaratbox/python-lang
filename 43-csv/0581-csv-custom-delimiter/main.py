import csv
import io

data = "a;b;c\n1;2;3\n"

# Configure the csv reader's delimiter to ';' to parse semicolon-delimited text.
rows = list(csv.reader(io.StringIO(data), delimiter=";"))

# rows[0] is the header; rows[1] is the data row.
# Join the data row's fields with commas.
print(",".join(rows[1]))
