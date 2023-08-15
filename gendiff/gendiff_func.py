from gendiff.parsing import parsing_data
from gendiff.formaters.stylish import stylishing
from gendiff.formaters.jsonutils import serializing
from gendiff.formaters.plain import plain


def generate_diff(file1_path, file2_path, format_name='stylish'):
    # Получаем данные из файлов
    path_name1 = file1_path
    path_name2 = file2_path
    data1 = parsing_data(path_name1)
    data2 = parsing_data(path_name2)
    # Сравниваем данные и формируем различия
    diff = collecting_diff(data1, data2)
    if format_name == 'stylish':
        result = stylishing(diff)
    elif format_name == 'plain':
        result = plain(diff)
    elif format_name == 'json':
        result = serializing(diff)
    return result


def convert_to_lowercase(data):
    # Проверяем, является ли значение булевым,
    # и преобразуем его к нижнему регистру
    if isinstance(data, bool):
        return str(data).lower()
    else:
        return data


def collecting_diff(data1, data2):
    # Создаем словарь для хранения различий
    diff = {}
    # Собираем и сортируем все уникальные ключи из обоих словарей
    keys = sorted(list(set(data1.keys()) | set(data2.keys())))
    # Проходим по всем ключам и сравниваем значения
    for key in keys:
        # Получаем значения для текущего ключа из каждого словаря
        value1 = convert_to_lowercase(data1.get(key, 'not_for_add_to_dict'))
        value2 = convert_to_lowercase(data2.get(key, 'not_for_add_to_dict'))
        # Собираем словарь со промаркерованными сходствами и различиями
        diff = marking_same_and_diff_values(key, value1, value2, diff)
    return diff


def marking_same_and_diff_values(key, value1, value2, diff):
    if not isinstance(value1, dict) and not isinstance(value2, dict):
        # Если значения равны,
        # добавляем их в diff как общее значения одного ключа
        if value1 == value2:
            diff[key] = value1
        else:
            # Иначе добавляем в значение ключа словарь
            # со старым и новым значением
            diff[key] = {'old_value': value1, 'new_value': value2}
    # Если одно из значений является словарем, а второе нет,
    # добавляем различия для первого вложенного словаря
    elif isinstance(value1, dict) and not isinstance(value2, dict):
        diff[key] = {'old_value': value1, 'new_value': value2}
    elif not isinstance(value1, dict) and isinstance(value2, dict):
        diff[key] = {'old_value': value1, 'new_value': value2}
    elif isinstance(value1, dict) and isinstance(value2, dict):
        # Если оба значения словари, рекурсивно сравниваем их
        # с помощью "замыкания" collecting_diff
        diff[key] = collecting_diff(value1, value2)
    return diff
