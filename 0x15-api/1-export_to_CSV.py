#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export data in the CSV format."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    file_name = "{}.csv".format(argv[1])
    user_id = int(argv[1])

    # get the info of the users and tasks by his id in dict format
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
                argv[1])).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                            argv[1])).json()

    # create and open a file and fill with the info below
    with open(file_name, mode='w') as csvfile:
        content = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            content.writerow(
                [user_id,
                    users.get('username'),
                    todo.get('completed'),
                    todo.get('title')])
