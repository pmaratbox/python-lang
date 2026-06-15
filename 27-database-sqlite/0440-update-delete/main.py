import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table users(id integer, name text)")
c.executemany("insert into users values(?,?)", [(1, "alice"), (2, "bob"), (3, "carol")])
c.execute("update users set name='robert' where id=2")
c.execute("delete from users where id=1")
for (i, n) in c.execute("select id,name from users order by id"):
    print(i, n)
