import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table users(id integer, name text)")
c.executemany(
    "insert into users values(?,?)",
    [(1, "alice"), (2, "bob"), (3, "carol")],
)
# Bind the parameter value 2 via real parameter binding (no string interpolation).
print(c.execute("select name from users where id=?", (2,)).fetchone()[0])
