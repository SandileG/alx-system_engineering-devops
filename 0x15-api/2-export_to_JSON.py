#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""

import json
import requests
import sys


def fetch_user_info(user_id):
    """Fetches user information from the JSONPlaceholder API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user information")
        sys.exit(1)
    user_data = user_response.json()
    return user_data


def fetch_todo_list(user_id):
    """Fetches the to-do list for the given user ID from the
    JSONPlaceholder API.
    """
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    todo_response = requests.get(todo_url, params=params)
    if todo_response.status_code != 200:
        print("Error fetching to-do list")
        sys.exit(1)
    todo_list = todo_response.json()
    return todo_list


def export_to_json(user_id, user_data, todo_list):
    """Exports user's to-do list to a JSON file."""
    json_data = {
    user_id: [{"task": task["title"], "completed": task["completed"], "username": user_data["username"]} for task in todo_list]
}

    filename = f"{user_id}.json"
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    user_data = fetch_user_info(user_id)
    todo_list = fetch_todo_list(user_id)
    export_to_json(user_id, user_data, todo_list)
