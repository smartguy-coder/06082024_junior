
class Person:
    def __init__(self, firstname: str, weight: float):
        self.name = firstname.title()
        self.weight = weight


person1 = Person('Alex', 3.600)
person2 = Person('John', 3.600)
person3 = Person(firstname='john', weight=4.600)

print()

print(person1)

print(id(person1))
print(id(person2))
