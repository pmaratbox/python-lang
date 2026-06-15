import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table t(n integer)")
c.isolation_level = None

c.execute("begin")
c.execute("insert into t values(1)")
c.execute("insert into t values(2)")
c.execute("commit")

c.execute("begin")
c.execute("insert into t values(3)")
c.execute("rollback")

for (n,) in c.execute("select n from t order by n"):
    print(n)
