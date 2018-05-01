#!/usr/bin/python3
'''
    Script to gather todo list for input user id and save to JSON format file
'''
if __name__ == "__main__":
    import requests
    import json

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users')

    user = user.json()

    dicts = {}

    for x in user:
        todo_list = []
        todo = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                x.get('id')))
        todo = todo.json()
        for y in todo:
            todo_list.append({'task': y.get('title'),
                              'completed': y.get('completed'),
                              'username': x.get('name')})
        dicts[x.get('id')] = todo_list

    with open("todo_all_employees.json", mode='w+', encoding='utf-8') as f:
        json.dump(dicts, f)
