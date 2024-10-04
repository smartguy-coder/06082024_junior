from pprint import pprint

# person_name = 'Alex'
# person_age = 16

person1 = {
    'name': 'John',
    'age': 20,
    'hobbies': [
        'soccer',
        'tennis',
    ]
}

person2 = {
    'name': 'Alex',
    'age': 15,
    'hobbies': [],
    'best_friend': {
        'name': 'Marta',
        'age': 11,
        'hobbies': [
            'tennis',
        ]
    }
}
animal = {'bread': 'cally'}

# pprint(person2)
# print(person2)

# age_person_1 = person1['age']
# print(age_person_1)
#
# age_person_2 = person2['age']
# print(age_person_2)
#
# age_of_best_friend_person_2 = person2['best_friend']['age']
# print(age_of_best_friend_person_2)

any_hobby_of_best_friend_person_2 = person2['best_friend']['hobbies'][0]
print(any_hobby_of_best_friend_person_2)
