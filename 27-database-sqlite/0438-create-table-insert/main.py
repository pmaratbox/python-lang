import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table users(id integer, name text)")
c.executemany("insert into users values(?,?)", [(1, "alice"), (2, "bob"), (3, "carol")])
for (name,) in c.execute("select name from users order by id"):
    print(name)
