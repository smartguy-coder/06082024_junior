
from datetime import datetime, timedelta


class Person:
    def __init__(self, firstname: str, weight: float):
        self.name = firstname.title()
        self.weight = weight
        # self.birthday = datetime.now()
        self.birthday = datetime(year=2012, month=11, day=1, hour=5)

    def say_age(self):
        time_difference = datetime.now() - self.birthday
        return f'Мені {time_difference.days // 365} років'

    @property
    def age(self):
        time_difference = datetime.now() - self.birthday
        return time_difference.days // 365

    def say_hello(self):
        return 'Hello'


person1 = Person('Alex', 3.600)
person2 = Person('John', 3.600)
person3 = Person(firstname='john', weight=4.600)

print(person1.birthday)
print(person1.name)
print(person1.__dict__)

person1.weight = 55
person1.hobby = ['tennis']

del person1.weight
print(person1.age)

person1.birthday = datetime(year=2002, month=11, day=1)
print(person1.age)
print(person1.say_age())
print(person1.say_hello())

# print(id(person1))
# print(id(person2))
