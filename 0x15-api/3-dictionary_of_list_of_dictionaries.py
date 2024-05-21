#!/usr/bin/python3
"""A script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("name")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        tasks = [
            {"task": t.get("title"), "completed": t.get("completed"),
             "username": username}
            for t in todos
        ]

        all_data[str(user_id)] = tasks

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w', encoding="utf-8") as f:
        json.dump(all_data, f)
