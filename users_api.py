import requests

# base
# url = 'https://dummyjson.com/users'
# response = requests.get(url)
# response_json = response.json()

# path param
# url = 'https://dummyjson.com/users/{user_id}'
# for user_id in range(1, 201):
#     this_url = url.format(user_id=user_id)
#     response = requests.get(this_url)
#     response_json = response.json()
#     print(response_json)

# query param
url = 'https://dummyjson.com/users'
params = {
    'limit': 3000,
    'skip': 0,
}

response = requests.get(url, params=params)
response_json = response.json()
users = response_json['users']

for user in users:
    user_address = user['address']
    city = user_address['city']
    if city == 'Denver':
        print(user_address)
