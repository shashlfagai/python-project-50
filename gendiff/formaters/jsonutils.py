import json


def serializing(diff):
    with open('diff.json', 'w') as data:
        data = json.dumps(diff)
    return data
