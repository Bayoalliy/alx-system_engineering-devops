#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """

import requests
from sys import argv

if __name__ == '__main__':
    NUMBER_OF_DONE_TASKS = 0

    url = "https://jsonplaceholder.typicode.com/"

    user = "{}/users/{}".format(url, argv[1])
    user_obj = requests.get(user)
    user_json = user_obj.json()
    EMPLOYEE_NAME = user_json.get("name")

    todo = "{}/todos?userId={}".format(url, argv[1])
    todo_obj = requests.get(todo)
    todo_json = todo_obj.json()
    TOTAL_NUMBER_OF_TASKS = len(todo_json)

    done_tasks = []
    for task in todo_json:
        if task.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            done_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
          EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for title in done_tasks:
        print("\t {}".format(title))
