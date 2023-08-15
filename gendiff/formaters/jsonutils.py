from gendiff.formaters.plain import plain


def serializing(diff):
    with open('diff.json','w') as output_file:
        output_file.write(plain(diff))
    return output_file
