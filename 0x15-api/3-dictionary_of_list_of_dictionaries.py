#!/usr/bin/python3
"""python script to fetch Rest API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    Users = response.json()

    dict_users = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dict_users[USER_ID] = []
        for task in tasks:
            dict_users[USER_ID].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": USERNAME
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict_users, file)
