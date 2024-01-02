#!/usr/bin/python3

"""
module: 0-gather_data_from_an_API
"""

import requests
import sys


def get_employee_todo_progress(id):
    """
        Returns the information about his/her TODO list
        progress using employess ID.
    """

    user_base_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    base_url = f'https://jsonplaceholder.typicode.com/todos'

    # request to API
    resp = requests.get(base_url)
    user_resp = requests.get(user_base_url)

    # check resp status code for success or otherwise
    if resp.status_code == 200 and user_resp.status_code == 200:
        data = resp.json()
        user_data = user_resp.json()

        # get user name
        name = user_data['name']
        completed_tasks = 0
        total_tasks = 0
        todos = []

        for task in data:
            if task["userId"] == id:
                total_tasks += 1
                if task["completed"] is True:
                    todos.append(task["title"])  # if completed... add
                    completed_tasks += 1

        print(f"Employee {name} is done with tasks", end='')
        print(f"({completed_tasks}/{total_tasks})")
        for t in todos:
            print(f"\t {t}")

    else:
        print("ERROR: Unable to fetch data")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: script <employee_id>")

    try:
        id = int(sys.argv[1])
        get_employee_todo_progress(id)
    except ValueError:
        print("ERROR: Wrong ID Type")
