import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table t(amount integer)")
c.executemany("insert into t values(?)", [(10,), (20,), (30,), (40,), (50,)])
r = c.execute(
    "select count(*),sum(amount),min(amount),max(amount) from t"
).fetchone()
for v in r:
    print(v)
