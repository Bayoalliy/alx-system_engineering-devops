#!/usr/bin/python3
""" Script that export data in the json format. """
import json
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

    dic = {}
    inner_dic = {}
    dic[USER_ID] = []

    for task in todo_json:
        inner_dic["task"] = task.get("title")
        inner_dic["completed"] = task.get("completed")
        inner_dic["username"] = USERNAME
        dic[USER_ID].append(inner_dic)
        inner_dic = {}

    j_dic = json.dumps(dic)

    file_name = "{}.json".format(USER_ID)
    f = open(file_name, "w")
    f.write(j_dic)
