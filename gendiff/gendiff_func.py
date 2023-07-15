from gendiff.parsing import parsing_data1, parsing_data2


def generate_diff(file1_path, file2_path):
    # Загружаем данные из
    # первого файла в словарей
    data1 = parsing_data1(file1_path)
    data2 = parsing_data2(file2_path)
    # Форматируем словарь
    diff1 = adding_file1_keys_and_diff_keys(data1, data2)
    diff2 = adding_file2_keys(data1, data2)
    diff = {**diff1, **diff2}
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
    sorted_keys = sorted(diff.keys(),
                         key=lambda k: k[2:] if k.startswith(('+', '-')) else k)
    for key in sorted_keys:
        sorted_diff[key] = diff[key]
    return sorted_diff


def adding_file1_keys_and_diff_keys(data1, data2):
    diff = {}
    for key in data1:
        if key not in data2:
            # Если ключ есть только в первом файле,
            # добавляем его в словарь с префиксом "-"
            diff['- ' + key] = data1[key]
        elif data1[key] != data2[key]:
            # Если значения по ключу отличаются,
            # добавляем ключ с префиксом "-" и значение из первого файла
            diff['- ' + key] = data1[key]
            # Добавляем ключ с префиксом "+" и значение из второго файла
            diff['+ ' + key] = data2[key]
        elif data1[key] == data2[key]:
            # Если ключи в первом и втором файлах равны,
            # то добавляем ключ и значение без префиксов
            diff[key] = data1[key]
    return diff


def adding_file2_keys(data1, data2):
    diff = {}
    for key in data2:
        if key not in data1:
            # Добавляем ключ с префиксом "+"
            # и значение из второго файла
            diff['+ ' + key] = data2[key]
    return diff
