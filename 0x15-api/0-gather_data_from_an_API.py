#!/usr/bin/python3
"""
Python script to retrieve an employee's TODO list progress from a REST API.
"""

import requests
import sys


def get_todo_list(employee_id):
    """
    Retrieves TODO list for given employee ID from the specified REST API.

    Args:
        employee_id (int): ID of employee whose TODO list is to be retrieved.

    Returns:
        dict: The TODO list in JSON format.
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}
    response = requests.get(url, params=params)
    return response.json()


def display_todo_progress(employee_id):
    """
    Displays the progress of an employee's TODO list.

    Args:
        employee_id (int): The ID of the employee.
    """
    todo_list = get_todo_list(employee_id)
    completed_tasks = [task for task in todo_list if task['completed']]
    total_tasks = len(todo_list)
    num_completed_tasks = len(completed_tasks)
    employee_name = todo_list[0]['username']

    print(f"{employee_name} is done ({num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    display_todo_progress(employee_id)
