#!/usr/bin/python3
"""
Retrieves and exports the to-do list of a given employee ID in CSV format.
"""

import requests
import csv
import sys


def get_todo_list(employee_id):
    """
    Retrieves the TODO list for the given employee ID
    from the specified REST API.

    Args:
        employee_id (int): The ID of the employee whose TODO
        list is to be retrieved.

    Returns:
        list: The TODO list in JSON format.
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}
    response = requests.get(url, params=params)
    return response.json()


def export_to_csv(employee_id, todo_list):
    """
    Exports the employee's TODO list to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        todo_list (list): The TODO list in JSON format.
    """
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames =
        ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in todo_list:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': task['username'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    todo_list = get_todo_list(employee_id)
    export_to_csv(employee_id, todo_list)
