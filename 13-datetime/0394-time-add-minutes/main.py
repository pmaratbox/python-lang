total = 10 * 60 + 45 + 90
h, m = divmod(total, 60)
print("{:02d}:{:02d}".format(h, m))
