#!/usr/bin/python3

"""
module: 2-export_to_JSON
"""

import json
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
        name = user_data['username']

        # get data for JSON
        json_data = {f"{id}": []}
        for task in data:
            if task["userId"] == id:
                task_completed_status = task["completed"]
                task_title = task["title"]
                json_data[f"{id}"].append(
                  {"task": task_title, "completed": task_completed_status,
                   "username": name})

        # Save data to JSON FILE
        json_file_name = f"{id}.json"
        with open(json_file_name, "w") as jsfile:
            json.dump(json_data, jsfile)

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
