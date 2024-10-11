import requests

todo_json_url = 'https://dummyjson.com/todos'

response = requests.get(todo_json_url)
response_json = response.json()

todos: list[dict] = response_json['todos']
# todos = response_json['todos']

completed = 0
for todo in todos:
    # print(todo)
    if todo['completed']:
        completed += 1

if todos:
    avg_comp = completed / len(todos)
    print(avg_comp)
