#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""

import csv
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


def export_to_csv(user_data, todo_list):
    """Exports user's to-do list to a CSV file."""
    filename = f"{user_data['id']}.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames =
        ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in todo_list:
            writer.writerow({
                "USER_ID": user_data["id"],
                "USERNAME": user_data["username"],
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    user_data = fetch_user_info(user_id)
    todo_list = fetch_todo_list(user_id)
    export_to_csv(user_data, todo_list)

    # Check number of tasks in CSV
    if len(todo_list) == sum(1 for _ in open(f"{user_id}.csv", "r")) - 1:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")

    # Check correct user ID and username retrieved
    user_id_in_csv, username_in_csv = None, None
    with open(f"{user_id}.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        first_row = next(reader)
        user_id_in_csv, username_in_csv = first_row[0], first_row[1]

    if user_id == user_id_in_csv and user_data["username"] == username_in_csv:
        print("User ID and Username: OK")
    else:
        print("User ID: Incorrect / Username: Incorrect")

    # Check correct output formatting
    with open(f"{user_id}.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        for index, row in enumerate(reader, start=1):
            expected_row =
            [user_data["id"], user_data["username"], 
            str(todo_list[index - 1]["completed"]),
            todo_list[index - 1]["title"]]
            if row != expected_row:
                print(f"Task {index} Formatting: Incorrect")
                break
        else:
            print("Formatting: OK")
