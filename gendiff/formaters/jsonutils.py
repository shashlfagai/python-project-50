from gendiff.formaters.stylish import stylishing


def serializing(diff):
    with open('diff.json', 'w') as output_file:
        output_file.write(stylishing(diff))
    return (
        'JSON file with diff is ready!\n'
        'Path to file:\n'
        '/python-project-50/diff.json'
        )
