#!/usr/bin/python3
'''
Script that uses a given REST API for a given employee ID
and returns information about his/her TODO list progress
'''
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + employee_id

    res = requests.get(url)
    employee_name = res.json().get("name")

    url_todo = url + "/todos"
    res = requests.get(url_todo)
    tasks = res.json()
    total_number_of_tasks = 0
    number_of_done_tasks = []

    for task in tasks:
        if task.get("completed"):
            number_of_done_tasks.append(task)
            total_number_of_tasks += 1

    print(f"Employee {employee_name} is done with\
            tasks({total_number_of_tasks}/{len(tasks)}):")

    for task in number_of_done_tasks:
        print(f"\t {task.get('title')}")
