import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table scores(value integer)")
c.executemany("insert into scores values(?)", [(50,), (90,), (70,), (30,), (100,), (20,)])
for (v,) in c.execute("select value from scores order by value desc limit 3"):
    print(v)
