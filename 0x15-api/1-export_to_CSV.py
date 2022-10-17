#!/usr/bin/python3
"""Export data to a CSV file"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    r = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    todos = requests.get(url).json()
    for task in todos:
        with open('{}.csv'.format(argv[1]), 'a') as f:
            f.write('"{}","{}","{}","{}"\n'
                    .format(argv[1], r.get('username'), task.get('completed'),
                            task.get('title')))
