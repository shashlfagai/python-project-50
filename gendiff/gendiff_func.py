from gendiff.parsing import parsing_data


def generate_diff(file1_path, file2_path):
    # Выполняем парсинг
    data1 = parsing_data(file1_path)
    data2 = parsing_data(file2_path)
    # Форматируем словарь
    diff_plus = collecting_diff_with_plus(data1, data2)
    diff_minus = collecting_diff_with_minus(data1, data2)
    no_diff = collecting_sames(data1, data2)
    diff = {**diff_plus, **diff_minus, **no_diff}
    sorted_diff = sort_diff(diff)
    formatted_diff = format_diff(sorted_diff, diff_minus, diff_plus)
    # Возвращаем отформатированную строку различий
    return formatted_diff


def format_diff(diff, diff_minus, diff_plus):
    lines = ['{']
    for key, value in diff.items():
        if key in diff_minus and diff[key] == diff_minus[key]:
            lines.append(f" - {key}: {value}")
        elif key in diff_plus and diff[key] == diff_plus[key]:
            lines.append(f" + {key}: {value}")
        else:
            lines.append(f"   {key}: {value}")
    lines.append('}')
    return '\n'.join(lines)


def sort_diff(diff):
    sorted_diff = {}
    sorted_keys = sorted(diff.keys())
    for key in sorted_keys:
        sorted_diff[key] = diff[key]
    return sorted_diff


def collecting_diff_with_plus(data1, data2):
    diff_with_plus = {}
    for key in data1:
        if key in data2 and data1[key] != data2[key]:
            # Добавляем ключ с префиксом "+" и значение из второго файла
            diff_with_plus[key] = data2[key]
    for key in data2:
        if key not in data1:
            # Добавляем ключ с префиксом "+"
            # и значение из второго файла
            diff_with_plus[key] = data2[key]
    return diff_with_plus


def collecting_diff_with_minus(data1, data2):
    diff_with_minus = {}
    for key in data1:
        if key not in data2:
            # Если ключ есть только в первом файле,
            # добавляем его в словарь с префиксом "-"
            diff_with_minus[key] = data1[key]
        if key in data2 and data1[key] != data2[key]:
                # Если значения по ключу отличаются,
                # добавляем ключ с префиксом "-" и значение из первого файла
                diff_with_minus[key] = data1[key]
    return diff_with_minus


def collecting_sames(data1, data2):
    no_diff = {}
    for key in data1:
        if key in data2 and data1[key] == data2[key]:
                # Если ключи в первом и втором файлах равны,
                # то добавляем ключ и значение без префиксов
                no_diff[key] = data1[key]
    return no_diff
    

def adding_file2_keys(data1, data2):
    diff = {}
    for key in data2:
        if key not in data1:
            # Добавляем ключ с префиксом "+"
            # и значение из второго файла
            diff[key] = data2[key]
    return diff
