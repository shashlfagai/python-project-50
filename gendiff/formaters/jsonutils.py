from gendiff.formaters.plain import plain
import json


def serializing(diff):
    formated_diff = plain(diff)
    with open('diff.json', 'w') as output_file:
        json.dump(formated_diff, output_file, indent=2)
    return output_file
