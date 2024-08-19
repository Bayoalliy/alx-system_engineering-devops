#!/usr/bin/python3
""" Script that export data in the CSV format. """
import csv
import requests
from sys import argv

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"
    user = "{}/users/{}".format(url, argv[1])
    user_obj = requests.get(user)
    user_json = user_obj.json()
    USERNAME = user_json.get("username")
    USER_ID = argv[1]

    todo = "{}/todos?userId={}".format(url, argv[1])
    todo_obj = requests.get(todo)
    todo_json = todo_obj.json()

    file_name = "{}.csv".format(argv[1])
    csvfile = open(file_name, "w", newline='')
    c = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
    lst = []
    for task in todo_json:
        lst.append("{}".format(USER_ID))
        lst.append(USERNAME)
        lst.append(task.get("completed"))
        lst.append(task.get("title"))
        c.writerow(lst)
        lst = []
