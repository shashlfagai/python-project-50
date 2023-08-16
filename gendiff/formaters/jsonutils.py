from gendiff.formaters.plain import plain


def serializing(diff):
    formated_diff = plain(diff)
    with open('diff.json', 'w') as output_file:
        output_file.write(formated_diff)
    return formated_diff
