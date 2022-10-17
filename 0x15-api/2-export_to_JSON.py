#!/usr/bin/python3
"""Export data to a JSON file"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    task_list = []
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    r = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    todos = requests.get(url).json()
    for task in todos:
        task.pop('id')
        task.pop('userId')
        task['task'] = task.pop('title')
        task.update({'username': r.get('username')})
        task_list.append(task)
    dict = {'{}'.format(argv[1]): task_list}
    with open('{}.json'.format(argv[1]), 'w') as f:
        f.write(json.dumps(dict))
