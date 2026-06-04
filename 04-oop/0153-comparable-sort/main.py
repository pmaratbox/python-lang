class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("alice", 30), Person("bob", 25)]
people.sort(key=lambda p: p.age)
print(" ".join(p.name for p in people))
