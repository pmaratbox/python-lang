people = [(1, "alice"), (2, "bob")]
by_id = {pid: name for pid, name in people}
print("id 2: " + by_id[2])
