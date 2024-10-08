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
    'vehicle': None,
    'age': 15,
    'hobbies': [],
    'best_friend': {
        'name': 'Marta',
        'age': 11,
        'hobbies': [
            'tennis',
        ]
    },
    'classes': None
}
animal = {'breed': 'cally'}

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

# CRUD

# Create
empty_dict = {}
empty_dict2 = dict()
not_empty_dict = dict(data=22)

# Read
person_2_name = person2['name']
person_2_surname = person2.get('surname')
person_2_vehicle = person2.get('vehicle', 'bicycle')
person_2_vehicle2 = person2.get('vehicle') or 'bicycle'
person_2_classes: list[str] = person2.get('classes', []) or []

# for element in person2.values():
# for element in person2.keys():
for key, value in person2.items():
    # dict_items([('name', 'Alex'), ('vehicle', None), ('age', 15), ('hobbies', []), ('best_friend', {'name': 'Marta', 'age': 11, 'hobbies': ['tennis']}), ('classes', None)])
    pass


# Update
# add elem
person2['car'] = 'Ferrari'
person2['age'] = 55

additional_data_person2 = {
    'car': 'Audi TT',
    'score': 98,
}

# person2 = person2 | additional_data_person2
person2 |= additional_data_person2

# Delete
# del person2['score']
score = person2.pop('score')
pass
