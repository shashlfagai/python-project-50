from gendiff.formaters.stylish import stylishing
import json


def serializing(diff):
    formated_diff = stylishing(diff)
    with open('diff.json', 'w') as output_file:
        output_file.write(json.dumps(formated_diff))
    return formated_diff
