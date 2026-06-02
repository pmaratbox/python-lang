import io

sb = io.StringIO()
for i, n in enumerate([1, 2, 3]):
    if i > 0:
        sb.write("-")
    sb.write(str(n))
print(sb.getvalue())
