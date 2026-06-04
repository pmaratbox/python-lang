import datetime

d = datetime.date(2000, 1, 1) + datetime.timedelta(days=3)
print(d.strftime("%A"))
