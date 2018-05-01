#!/usr/bin/python3
'''
    Script to gather todo list for input user id and save to JSON format file
'''
import requests
import json

user = requests.get(
    'https://jsonplaceholder.typicode.com/users')

user = user.json()

dicts = {}

for x in user:
    todo_list = []
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(x['id']))
    todo = todo.json()
    for y in todo:
        todo_list.append({'task': y['title'],
                          'completed': y['completed'], 'username': x['name']})
    dicts[x['id']] = todo_list

with open("todo_all_employees.json", mode='w+', encoding='utf-8') as f:
    json.dump(dicts, f)
