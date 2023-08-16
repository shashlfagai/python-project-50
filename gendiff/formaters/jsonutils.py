from gendiff.formaters.plain import plain
import json


def serializing(diff):
    with open('diff.json', 'w') as output_file:
        json.dump(diff, output_file)
    return diff
