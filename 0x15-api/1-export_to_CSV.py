#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API and convert the response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated with the given user ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write the to-do list items to a CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow
            ([user_id, username, todo.get("completed"), todo.get("title")])

    # Count the number of tasks written to the CSV file
    num_tasks_in_csv = len(todos)

    print("Number of tasks in CSV: {}".format("OK" if num_tasks_in_csv == len(todos) else "Incorrect"))
