#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script
 to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    file_name = "{}.json".format(argv[1])
    user_id = int(argv[1])
    data = {user_id: []}
    aux_dict = {}

    # get the info of the users and tasks by his id in dict format
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
                argv[1])).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                argv[1])).json()

    for todo in todos:
        aux_dict["task"] = todo.get("title")
        aux_dict["completed"] = todo.get("completed")
        aux_dict["username"] = users.get("username")
        data[user_id].append(aux_dict)
        aux_dict = {}

    # create and open a file and fill with the info above
    with open(file_name, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)
