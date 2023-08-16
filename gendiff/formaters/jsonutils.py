from gendiff.formaters.stylish import stylishing
import json
import pickle


def serializing(diff):
    with open('diff.json', 'w') as data:
        data = json.dumps(diff)
    return data
