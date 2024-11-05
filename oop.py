
from datetime import datetime, timedelta


class Person:
    rights_list = ['one', 'two']
    DNA = 'XYC-HJG-JMM'
    population = []

    @staticmethod
    def add_two_numbers(first, second):
        return first + second

    @classmethod
    def get_people_with_min_weight(cls, min_weight: float):
        valid_people = []
        for person in cls.population:
            if person.weight >= min_weight:
                valid_people.append(person)
        print(88888888888888888888888)
        return valid_people

    def __init__(self, firstname: str, weight: float):
        self.name = firstname.title()
        self.weight = weight
        # self.birthday = datetime.now()
        self.birthday = datetime(year=2012, month=11, day=1, hour=5)

        self.population.append(self)

    def say_age(self):
        time_difference = datetime.now() - self.birthday
        return f'Мені {time_difference.days // 365} років'

    @property
    def age(self):
        time_difference = datetime.now() - self.birthday
        return time_difference.days // 365

    def say_hello(self):
        return 'Hello'

    def __str__(self):
        return f'<{self.name} with weight {self.weight}>'

    __repr__ = __str__

    def __del__(self):
        print(self)
        self.population.remove(self)
        print(self.population)


person1 = Person('Alex', 3.600)
person2 = Person('John', 3.200)
person3 = Person(firstname='john', weight=4.600)


print(person1.add_two_numbers(2, 10))
print(Person.add_two_numbers(2, 15))

print(person1.DNA)
print(Person.DNA)
person1.DNA = 'some DNA'
person1.rights_list.append('three')

print(person1.birthday)
print(person1.name)
print(person1.__dict__)
print(person2.__dict__)

person1.weight = 55
print(Person.get_people_with_min_weight(22))
person1.hobby = ['tennis']

# del person1.weight
# del person1
# print(person1.age)

# person1.birthday = datetime(year=2002, month=11, day=1)
# print(person1.age)
# print(person1.say_age())
# print(person1.say_hello())
pass
# print(id(person1))
# print(id(person2))


print(Person.get_people_with_min_weight(22))
