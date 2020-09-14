#!/usr/bin/python3
"""Write a Python script that, using this REST API,
 for a given employee ID, returns information about
  his/her to-do list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    # get the employee name by his id
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    for user in users:
        if user['id'] == int(argv[1]):
            EMPLOYEE_NAME = user['name']
            break

    # get the neccesary information of the todo api
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for todo in todos:
        if todo['userId'] == int(argv[1]):
            if todo['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo['title'])
            TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS))

    for quote in TASK_TITLE:
        print("\t {}".format(quote))
