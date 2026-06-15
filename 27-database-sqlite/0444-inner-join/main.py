import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table users(id integer, name text)")
c.execute("create table orders(user_id integer, item text)")
c.executemany("insert into users values(?,?)", [(1, "alice"), (2, "bob")])
c.executemany("insert into orders values(?,?)", [(1, "book"), (2, "pen"), (1, "lamp")])
for (name, item) in c.execute(
    "select u.name,o.item from orders o join users u on u.id=o.user_id order by u.name,o.item"
):
    print(name, item)
