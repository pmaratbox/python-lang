class Animal:
    def speak(self) -> str:
        return "some sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"

print("animal:", Animal().speak())
print("dog:", Dog().speak())
