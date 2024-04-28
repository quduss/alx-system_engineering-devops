#!/usr/bin/python3
"""Gives the todo list of an employee. The id of the employee
is passed as an argument"""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    for a in todos:
        a["name"] = user.get("username")
        del a["id"]

    csv_file = f"{user_id}.csv"

    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["userId", "name", "completed", "title"],
            quoting=csv.QUOTE_ALL
        )

        for row in todos:
            writer.writerow(row)
