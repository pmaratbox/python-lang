import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table inv(item text primary key, qty integer)")
c.execute("insert into inv values('apple',5)")
c.execute("insert into inv values('apple',5) on conflict(item) do update set qty=qty+excluded.qty")
c.execute("insert into inv values('banana',3) on conflict(item) do update set qty=qty+excluded.qty")
for (item, qty) in c.execute("select item,qty from inv order by item"):
    print(item, qty)
