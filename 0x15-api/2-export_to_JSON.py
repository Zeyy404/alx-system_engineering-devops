#!/usr/bin/python3
"""A script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress."""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    username = user.get("username")
    tasks = [
        {"task": t.get("title"), "completed": t.get("completed"), "username": username}
        for t in todos
    ]
    json_data = {str(employee_id): tasks}

    file_name = "{}.json".format(employee_id)
    with open(file_name, mode='w', encoding="utf-8") as f:
        json.dump(json_data, f)
