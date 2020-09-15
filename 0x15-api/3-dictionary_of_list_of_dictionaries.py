#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script
 to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    aux_dict = {}
    data = {}

    # get the info of the users and tasks by his id in dict format
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    for user in users:
        data[user.get('id')] = []
        aux_dict[user.get('id')] = user.get('username')

    for todo in todos:
        task_dict = {}
        task_dict["task"] = todo.get('title')
        task_dict["completed"] = todo.get("completed")
        task_dict['username'] = aux_dict.get(todo.get('userId'))
        data.get(todo.get('userId')).append(task_dict)

    # for user in users:
    #     data[user.get("id")] = []
    #     for todo in todos:
    #         aux_dict["username"] = user.get("username")
    #         aux_dict["task"] = todo.get("title")
    #         aux_dict["completed"] = todo.get("completed")
    #         data[user.get("id")].append(aux_dict)
    #         aux_dict = {}

    # create and open a file and fill with the info above
    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)
