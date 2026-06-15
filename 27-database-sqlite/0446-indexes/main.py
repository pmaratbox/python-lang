import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table products(id integer, sku text, price integer)")
c.executemany("insert into products values(?,?,?)", [(1, "A", 100), (2, "B", 200), (3, "C", 300)])
c.execute("create index idx_sku on products(sku)")
print(c.execute("select price from products where sku=?", ("B",)).fetchone()[0])
