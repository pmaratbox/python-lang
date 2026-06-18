import csv, io

buf = io.StringIO()
writer = csv.writer(buf)
writer.writerow(["name", "age"])
writer.writerow(["Alice", "30"])

# csv.writer emits \r\n line terminators; normalize and strip the trailing newline.
print(buf.getvalue().replace("\r\n", "\n").rstrip("\n"))
