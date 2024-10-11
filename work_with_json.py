import json

location = {
    'area_name': 'Одеська область',
    'population': 2_200_006,
    'image': '⚓'
}

# dict -> json str
json_str = json.dumps(location)

# json str -> dict
dict_from_json = json.loads(json_str)

# json into file
# with open('data.json', mode='w') as file:
#     json.dump(location, file, indent=4)

# file into json
with open('data.json', mode='r') as file:
    data_from_file = json.load(file)
