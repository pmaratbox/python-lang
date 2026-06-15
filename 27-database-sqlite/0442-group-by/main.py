import sqlite3

c = sqlite3.connect(":memory:")
c.execute("create table sales(category text, amount integer)")
c.executemany(
    "insert into sales values(?,?)",
    [("a", 10), ("b", 20), ("a", 30), ("b", 5), ("a", 2)],
)
for (category, total) in c.execute(
    "select category,sum(amount) from sales group by category order by category"
):
    print(category, total)
