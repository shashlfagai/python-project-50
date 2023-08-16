from gendiff.formaters.plain import plain
import json


def serializing(diff):
    with open('diff.json', 'w') as output_file:
         output_file.write(json.dump(diff))
    return diff
