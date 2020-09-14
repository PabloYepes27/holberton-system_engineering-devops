#!/usr/bin/python3
import json
import requests
from sys import argv

EMPLOYEE_NAME = ""
NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
TASK_TITLE = []

response_user = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response_user.text)
for user in users:
    if user['id'] == int(argv[1]):
        EMPLOYEE_NAME = user['name']
        break

response_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response_todo.text)
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
