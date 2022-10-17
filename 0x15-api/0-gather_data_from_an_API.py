#!/usr/bin/python3
"""Gather data using the REST API"""
import requests
from sys import argv

if __name__ == '__main__':
    complete = 0
    complete_list = []
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    r = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    todos = requests.get(url).json()
    for task in todos:
        if task.get('completed'):
            complete += 1
            complete_list.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(r.get('name'), complete, len(todos)))
    for task in complete_list:
        print('\t {}'.format(task))
