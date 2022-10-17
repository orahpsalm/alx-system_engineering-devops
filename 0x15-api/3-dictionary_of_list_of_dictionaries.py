#!/usr/bin/python3
"""Export data to a JSON file"""
import json
import requests


if __name__ == '__main__':
    dict = {}
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url).json()
    for user in response:
        task_list = []
        todos = requests.get(url + str(user.get('id')) + '/todos').json()
        for task in todos:
            task.pop('id')
            task.pop('userId')
            task['task'] = task.pop('title')
            task.update({'username': user.get('username')})
            task_list.append(task)
        dict.update({'{}'.format(user.get('id')): task_list})
    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(dict))
