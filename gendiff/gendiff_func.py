import itertools
from gendiff.parsing import parsing_data


def generate_diff(file1_path, file2_path):
    path_name1 = file1_path
    path_name2 = file2_path 
    data1 = parsing_data(path_name1)
    data2 = parsing_data(path_name2)
    diff = collecting_diff(data1, data2)
    
    return diff


def collecting_diff(data1, data2, depth=1):
    diff = ["{"]
    deep_indent = '    ' * depth
    deep_indent_minus = deep_indent[:-2] + '- '
    deep_indent_plus = deep_indent[:-2] + '+ '
    finish_of_deep_indent = '    ' * (depth - 1) + "}"
    keys = sorted(list(set(data1.keys()) | set(data2.keys())))
    for key in keys:
        value1 = convert_to_lowercase(data1.get(key, 'not_for_add_to_dict'))
        value2 = convert_to_lowercase(data2.get(key, 'not_for_add_to_dict'))
        if not isinstance(value1, dict) and not isinstance(value2, dict):
            if value1 == 'not_for_add_to_dict':
                diff.append(f'{deep_indent_plus}{key}: {value2}')
            elif value2 == 'not_for_add_to_dict':
                diff.append(f'{deep_indent_minus}{key}: {value1}')
            elif value1 == value2:
                diff.append(f'{deep_indent}{key}: {value1}')
            elif value1 != value2:
                diff.append(f'{deep_indent_minus}{key}: {value1}\n{deep_indent_plus}{key}: {value2}')
        elif isinstance(value1, dict) and not isinstance(value2, dict):
            if value2 == 'not_for_add_to_dict':
                nested_value = diff_from_value(value1, depth)
                diff.append(f'{deep_indent_minus}{key}: {{\n{nested_value}')
                diff.append(f'{deep_indent}}}')
            else:
                nested_value = diff_from_value(value1, depth)
                diff.append(f'{deep_indent_minus}{key}: {{\n{nested_value}\n{deep_indent}}}\n{deep_indent_plus}{key}: {value2}')
        elif not isinstance(value1, dict) and isinstance(value2, dict):
            if value1 != 'not_for_add_to_dict':
                nested_value = diff_from_value(value2, depth)
                diff.append(f'{deep_indent_minus}{key}: {{\n{nested_value}\n{deep_indent}}}\n{deep_indent_plus}{key}: {value2}')
            else:
                nested_value = diff_from_value(value2, depth)
                diff.append(f'{deep_indent_plus}{key}: {{\n{nested_value}\n{deep_indent}}}')
        elif isinstance(value1, dict) and isinstance(value2, dict):
            nested_value =  collecting_diff(value1, value2, (depth + 1))
            diff.append(f'{deep_indent}{key}: {nested_value}')
            
    diff.append(finish_of_deep_indent)
    result = itertools.chain(diff)
    return '\n'.join(result)
    # return result


def convert_to_lowercase(data):
    if isinstance(data, bool):
        return str(data).lower()
    else:
        return data


def diff_from_value(value, depth):
    deep_indent_for_dict_value = '    ' * (depth + 1)
    nested_value = []
    for k, v in value.items():
        if isinstance(v, dict):
            nested_value.append(f'{deep_indent_for_dict_value}{k}: {{\n{diff_from_value(v, (depth + 1))}\n{deep_indent_for_dict_value}}}')
        else:
            nested_value.append(f'{deep_indent_for_dict_value}{k}: {v}')
    nested_value = '\n'.join(itertools.chain(nested_value))
    return nested_value
