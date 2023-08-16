from gendiff.formaters.stylish import stylishing
import json


def serializing(diff):
    formated_diff = stylishing(diff)
    with open('diff.json', 'w') as output_file:
        json.dump(formated_diff, output_file)
    return diff
