#!/usr/bin/python3
'''
    Script to gather todo list for input user id
'''
import requests
from sys import argv

todo = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

user = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))

todo = todo.json()
user = user.json()

count = 0
new = []
for x in todo:
    if x['completed']:
        new.append(x)
        count += 1

print('Employee {} is done with tasks ({}/{}):'.format(
    user['name'], count, len(todo)))

for y in new:
    print('\t {}'.format(y['title']))
