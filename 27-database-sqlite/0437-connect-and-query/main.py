import sqlite3

conn = sqlite3.connect(":memory:")
result = conn.execute("select 42").fetchone()[0]
print(result)
conn.close()
