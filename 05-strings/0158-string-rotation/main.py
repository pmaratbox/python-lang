a = "abcd"
b = "cdab"
is_rotation = len(a) == len(b) and b in (a + a)
print("yes" if is_rotation else "no")
