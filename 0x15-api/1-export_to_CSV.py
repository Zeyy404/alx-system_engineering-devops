#!/usr/bin/python3
"""A script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress."""
import csv
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
    csv_data = [
        [employee_id, username, t.get("completed"), t.get("title")]
        for t in todos
    ]

    file_name = "{}.csv".format(employee_id)
    with open(file_name, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(csv_data)
