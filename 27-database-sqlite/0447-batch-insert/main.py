import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("create table t(n integer)")

with conn:
    conn.executemany(
        "insert into t values(?)",
        [(i,) for i in range(1, 1001)],
    )

count = conn.execute("select count(*) from t").fetchone()[0]
print(count)
conn.close()
