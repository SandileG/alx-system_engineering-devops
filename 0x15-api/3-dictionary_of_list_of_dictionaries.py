import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()

    all_data = {}
    for user in users:
        user_id = str(user['id'])
        url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        response = requests.get(url)
        tasks = response.json()

        user_tasks = []
        for task in tasks:
            user_tasks.append({
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            })

        all_data[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_data, file, indent=4)
