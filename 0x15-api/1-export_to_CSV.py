#!/usr/bin/python3
'''
    Script to gather todo list for input user id and save to csv format file
'''
import requests
from sys import argv

todo = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

user = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))

todo = todo.json()
user = user.json()

with open("{}.csv".format(argv[1]), mode='w+', encoding='utf-8') as f:
    for x in todo:
        f.write('"{}","{}","{}","{}"\n'.format(
            user['id'], user['name'], x['completed'], x['title']))
