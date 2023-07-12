import json


def generate_diff(file1_path, file2_path):
    # Открываем файлы и загружаем их содержимое в словари
    with open(file1_path) as file1, open(file2_path) as file2:
        data1 = json.load(file1)  # Загружаем данные из первого файла в словарь data1
        data2 = json.load(file2)  # Загружаем данные из второго файла в словарь data2

    diff = {}  # Инициализируем пустой словарь для хранения различий

    # Сравниваем данные из двух словарей и формируем словарь различий
    for key in data1:
        if key not in data2:
            diff['- ' + key] = data1[key]  # Если ключ есть только в первом файле, добавляем его в словарь с префиксом "-"
        elif data1[key] != data2[key]:
            diff['- ' + key] = data1[key]  # Если значения по ключу отличаются, добавляем ключ с префиксом "-" и значение из первого файла
            diff['+ ' + key] = data2[key]  # Добавляем ключ с префиксом "+" и значение из второго файла
        elif data1[key] == data2[key]:
            diff[key] = data1[key] # Если ключи в первом и втором файлах равны, то добавляем ключ и значение без префиксов

    # Добавляем в словарь различий ключи, которых нет в первом словаре, но есть во втором
    for key in data2:
        if key not in data1:
            diff['+ ' + key] = data2[key]  # Добавляем ключ с префиксом "+" и значение из второго файла

    # Форматируем словарь 
    sorted_diff = sort_diff(diff)
    formatted_diff = format_diff(sorted_diff)

    # Возвращаем отформатированную строку различий
    return formatted_diff


def format_diff(diff):
    lines = ['{']
    for key, value in diff.items():
        if key.startswith('- '):
            lines.append(f" - {key[2:]}: {value}")
        elif key.startswith('+ '):
            lines.append(f" + {key[2:]}: {value}")
        else:
            lines.append(f"   {key}: {value}")
    lines.append('}')
    return '\n'.join(lines)



def sort_diff(diff):
    sorted_diff = {}
    sorted_keys = sorted(diff.keys(), key=lambda k: k[2:] if k.startswith(('+', '-')) else k)
    for key in sorted_keys:
        sorted_diff[key] = diff[key]
    return sorted_diff