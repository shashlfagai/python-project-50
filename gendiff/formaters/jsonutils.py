from gendiff.formaters.stylish import stylishing


def serializing(diff):
    with open('diff.json', 'w') as output_file:
        output_file.write(stylishing(diff))
    return output_file
