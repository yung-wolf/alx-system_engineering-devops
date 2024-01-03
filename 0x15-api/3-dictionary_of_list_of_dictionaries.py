#!/usr/bin/python3

"""
module: 3-dictionary_of_list_of_dictionaries
"""

import json
import requests
import sys


def get_employee_todo_progress():
    """
        Returns the information about his/her TODO list
        progress using employess ID.
    """

    user_base_url = 'https://jsonplaceholder.typicode.com/users/'
    base_url = 'https://jsonplaceholder.typicode.com/todos'

    # request to API
    user_resp = requests.get(user_base_url)
    todo_resp = requests.get(base_url)

    # check resp status code for success or otherwise
    if user_resp.status_code == 200 and todo_resp.status_code == 200:
        usr_data = user_resp.json()
        tds_data = todo_resp.json()

        json_data = dict()

        # get usr_data for JSON
        for user in usr_data:
            user_id = user["id"]
            username = user['username']

            json_data[str(user_id)] = []

            for task in tds_data:
                if task['userId'] == user_id:
                    task_completed_status = str(task["completed"])
                    task_title = task["title"]
                    json_data[str(user_id)].append(
                        {"username": username, "task": task_title,
                         "completed": task_completed_status}
                    )

        # Save data to JSON FILE
        json_file_name = "todo_all_employees.json"
        with open(json_file_name, "w") as jsfile:
            json.dump(json_data, jsfile)

    else:
        print("ERROR: Unable to fetch data")
        sys.exit(1)


if __name__ == "__main__":
    get_employee_todo_progress()
