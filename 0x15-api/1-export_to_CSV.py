#!/usr/bin/python3

"""
module: 0-gather_data_from_an_API
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Returns the information about his/her TODO list
    progress using employess ID.
    """

    user_base_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    base_url = 'https://jsonplaceholder.typicode.com/todos'

    # Request to API
    user_resp = requests.get(user_base_url)
    todo_resp = requests.get(base_url)

    # Check response status code for success or otherwise
    if user_resp.status_code == 200 and todo_resp.status_code == 200:
        user_data = user_resp.json()
        todo_data = todo_resp.json()

        # Get user details
        username = user_data['username']

        # Create CSV data using list comprehension
        csv_data = [
            [str(employee_id), username, str(task['completed']), task['title']]
            for task in todo_data
            if task['userId'] == employee_id
        ]

        # Save data to CSV file
        csv_file_name = f"{employee_id}.csv"
        with open(csv_file_name, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerows(csv_data)

    else:
        print("ERROR: Unable to fetch data")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: script <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("ERROR: Wrong ID Type")
