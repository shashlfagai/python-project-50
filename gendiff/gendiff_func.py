import itertools
from gendiff.parsing import parsing_data


def generate_diff(file1_path, file2_path):
    # Получаем данные из файлов
    path_name1 = file1_path
    path_name2 = file2_path
    data1 = parsing_data(path_name1)
    data2 = parsing_data(path_name2)
    # Сравниваем данные и формируем различия
    diff = collecting_diff(data1, data2)
    return diff


def collecting_diff(data1, data2, depth=1):
    # Создаем список для хранения различий
    diff = ["{"]
    # Задаем отступы для форматирования вывода различий
    deep_indent = '    ' * depth
    deep_indent_minus = deep_indent[:-2] + '- '
    deep_indent_plus = deep_indent[:-2] + '+ '
    finish_of_deep_indent = '    ' * (depth - 1) + "}"
    # Получаем все уникальные ключи из обоих словарей
    keys = sorted(list(set(data1.keys()) | set(data2.keys())))
    # Проходим по всем ключам и сравниваем значения
    for key in keys:
        # Получаем значения для текущего ключа из каждого словаря
        value1 = convert_to_lowercase(data1.get(key, 'not_for_add_to_dict'))
        value2 = convert_to_lowercase(data2.get(key, 'not_for_add_to_dict'))
        # Если значения не являются словарями,
        # добавляем различия для простых значений
        if not isinstance(value1, dict) and not isinstance(value2, dict):
            diff.extend(diff_of_simple_values
                        (key, value1, value2, deep_indent,
                         deep_indent_plus, deep_indent_minus))
        # Если первое значение является словарем, а второе нет,
        # добавляем различия для первого вложенного словаря
        elif isinstance(value1, dict) and not isinstance(value2, dict):
            diff.extend(diff_of_first_deep_value
                        (key, value1, value2, deep_indent,
                         deep_indent_minus, deep_indent_plus, depth))
        # Если второе значение является словарем, а первое нет,
        # добавляем различия для второго вложенного словаря
        elif not isinstance(value1, dict) and isinstance(value2, dict):
            diff.extend(diff_of_second_deep_value
                        (key, value1, value2, deep_indent,
                         deep_indent_minus, deep_indent_plus, depth))
        # Если оба значения являются словарями,
        # вызываем рекурсивно функцию collecting_diff
        # для сравнения вложенных словарей
        elif isinstance(value1, dict) and isinstance(value2, dict):
            nested_value = collecting_diff(value1, value2, (depth + 1))
            diff.append(f'{deep_indent}{key}: {nested_value}')
    # Закрываем уровень вложенности словаря
    diff.append(finish_of_deep_indent)
    # Объединяем список различий и возвращаем его в виде строки
    result = itertools.chain(diff)
    return '\n'.join(result)


def convert_to_lowercase(data):
    # Проверяем, является ли значение булевым,
    # и преобразуем его к нижнему регистру
    if isinstance(data, bool):
        return str(data).lower()
    else:
        return data


def diff_from_value(value, depth):
    # Рекурсивно обрабатываем словарь для формирования списка с различиями
    deep_indent_for_dict_value = '    ' * (depth + 1)
    nested_value = []
    for k, v in value.items():
        if isinstance(v, dict):
            nested_value.append(f'{deep_indent_for_dict_value}{k}: {{\n'
                                f'{diff_from_value(v, (depth + 1))}\n'
                                f'{deep_indent_for_dict_value}}}')
        else:
            nested_value.append(f'{deep_indent_for_dict_value}{k}: {v}')
    nested_value = '\n'.join(itertools.chain(nested_value))
    return nested_value


def diff_of_simple_values(key, value1, value2, deep_indent,
                          deep_indent_plus, deep_indent_minus):
    # Формируем список с различиями для простых значений (не словарей)
    diff = []
    if value1 == 'not_for_add_to_dict':
        diff.append(f'{deep_indent_plus}{key}: {value2}')
    elif value2 == 'not_for_add_to_dict':
        diff.append(f'{deep_indent_minus}{key}: {value1}')
    elif value1 == value2:
        diff.append(f'{deep_indent}{key}: {value1}')
    elif value1 != value2:
        diff.append(f'{deep_indent_minus}{key}: {value1}\n'
                    f'{deep_indent_plus}{key}: {value2}')
    return diff


def diff_of_first_deep_value(key, value1, value2, deep_indent,
                             deep_indent_minus, deep_indent_plus, depth):
    # Формируем список с различиями для первого вложенного словаря
    diff = []
    if value2 == 'not_for_add_to_dict':
        nested_value = diff_from_value(value1, depth)
        diff.append(f'{deep_indent_minus}{key}: {{\n{nested_value}')
        diff.append(f'{deep_indent}}}')
    else:
        nested_value = diff_from_value(value1, depth)
        diff.append(f'{deep_indent_minus}{key}: {{\n'
                    f'{nested_value}\n{deep_indent}}}\n'
                    f'{deep_indent_plus}{key}: {value2}')
    return diff


def diff_of_second_deep_value(key, value1, value2, deep_indent,
                              deep_indent_minus, deep_indent_plus, depth):
    # Формируем список с различиями для второго вложенного словаря
    diff = []
    if value1 == 'not_for_add_to_dict':
        nested_value = diff_from_value(value2, depth)
        diff.append(f'{deep_indent_plus}{key}: {{\n{nested_value}')
        diff.append(f'{deep_indent}}}')
    else:
        nested_value = diff_from_value(value2, depth)
        diff.append(f'{deep_indent_minus}{key}: {{\n'
                    f'{nested_value}\n{deep_indent}}}\n'
                    f'{deep_indent_plus}{key}: {value2}')
    return diff
