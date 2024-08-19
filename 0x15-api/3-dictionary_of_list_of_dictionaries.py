#!/usr/bin/python3
""" Script that export data in the json format. on steroids """
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = "{}/users/".format(url)
    users_obj = requests.get(users)
    users_json = users_obj.json()

    dic = {}
    for user in users_json:
        USERNAME = user.get("username")
        USER_ID = user.get("id")

        todo = "{}/todos?userId={}".format(url, USER_ID)
        todo_obj = requests.get(todo)
        todo_json = todo_obj.json()

        inner_dic = {}
        dic[USER_ID] = []

        for task in todo_json:
            inner_dic["task"] = task.get("title")
            inner_dic["completed"] = task.get("completed")
            inner_dic["username"] = USERNAME
            dic[USER_ID].append(inner_dic)
            inner_dic = {}

    j_dic = json.dumps(dic)

    f = open("todo_all_employees.json", "w")
    f.write(j_dic)
