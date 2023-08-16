from gendiff.formaters.stylish import stylishing
import json


def serializing(diff):
    with open('diff.json', 'w') as output_file:
        output_file.write(json.dumps(diff))
    return diff
