#!/usr/bin/python3
'''
    Script to gather todo list for input user id and save to JSON format file
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    todo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))

    todo = todo.json()
    user = user.json()

    new = {}
    temp = []
    for x in todo:
        temp.append({'task': x.get('title'),
                     'completed': x.get('completed'),
                     'username': user.get('name')})
    new[argv[1]] = temp

    with open("{}.json".format(argv[1]), mode='w+', encoding='utf-8') as f:
        json.dump(new, f)
