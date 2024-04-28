#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            x.get("id"): [{
                "task": a.get("title"),
                "completed": a.get("completed"),
                "username": x.get("username")
            } for a in requests.get(url + "todos",
                                    params={"userId": x.get("id")}).json()]
            for x in users}, jsonfile)
