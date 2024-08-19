#!/usr/bin/python3
"""
This module prints information about an employee
TODO list progress. based on his/her ID to the standard output
"""
import json
from sys import argv
from urllib import request

if __name__ == '__main__'
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    with request.urlopen('https://jsonplaceholder.typicode.com/todos/') as res:
        data = res.read()
        data_str = data.decode('utf-8')
        todos = json.loads(data_str)

    with request.urlopen('https://jsonplaceholder.typicode.com/users/') as res:
        data = res.read()
        data_str = data.decode('utf-8')
        users = json.loads(data_str)


    for emp in users:
        if emp["id"] == int(argv[1]):
            EMPLOYEE_NAME = emp['name']

    for task in todos:
            if task["userId"] == int(argv[1]):
                TOTAL_NUMBER_OF_TASKS += 1
                if task["completed"] is True:
                    NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(
          EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in todos:
        if task["userId"] == int(argv[1]):
            if task["completed"] is True:
                print("\t {}".format(task["title"]))
