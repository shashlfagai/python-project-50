def plain(diff):
    # Инициализируем отредактированую строку различий
    formatted_diff = formatting_diff(diff)
    # Убираем запятые
    formatted_diff = formatted_diff.replace(',', '')
    # Удаляем пустые строки
    formatted_diff = '\n'.join(
        line for line in formatted_diff.split('\n') if line
    )
    return formatted_diff


def formatting_diff(diff, way=''):
    formatted_diff = ''
    for k, v in diff.items():
        if not isinstance(v, dict):
            continue
        else:
            # Если у текущего элемента есть ключи 'new_value' или 'old_value',
            # используем функцию formatting_diff_of_flat_dict
            # для форматирования
            if 'new_value' in v or 'old_value' in v:
                formatted_diff = formatting_diff_of_flat_dict(
                    k, v, formatted_diff, way
                )
            else:
                # Если ключи 'new_value' и 'old_value' отсутствуют,
                # рекурсивно вызываем функцию formatting_diff
                # для обработки вложенных элементов
                nested_value = formatting_diff(v, way + f'{k}.')
                formatted_diff += nested_value
    return formatted_diff


def formatting_diff_of_flat_dict(k, v, formatted_diff, way):
    # Добавляем ключ к текущему пути
    way += k
    # Форматируем старое и новое значения с помощью соответствующих функций
    old_value = formatting_old_value(v['old_value'])
    new_value = formatting_new_value(v['new_value'])
    # Проверяем наличие ключей 'new_value' и 'old_value'
    if v["new_value"] == 'not_for_add_to_dict':
        # Если ключ 'new_value' указывает на 'not_for_add_to_dict',
        # значит значение было удалено
        formatted_diff += (f"Property '{way}' was removed\n")
    elif v['old_value'] == 'not_for_add_to_dict':
        # Если ключ 'old_value' указывает на 'not_for_add_to_dict',
        # значит значение было добавлено
        formatted_diff += (
            f"Property '{way}' was added with value: "
            f"{new_value}\n"
        )
    else:
        # В остальных случаях значение было обновлено,
        # указываем старое и новое значение
        formatted_diff += (
            f"Property '{way}' was updated. "
            f"From {old_value} to {new_value}\n"
        )
    return formatted_diff


def formatting_old_value(old_value):
    if old_value == 'null':
        old_value = old_value.strip("'")
    elif old_value == 'true':
        old_value = old_value.strip("'")
    elif old_value == 'false':
        old_value = old_value.strip("'")
    elif isinstance(old_value, dict):
        old_value = '[complex value]'
    elif isinstance(old_value, str):
        old_value = (f"'{old_value}'")
    return old_value


def formatting_new_value(new_value):
    if new_value == 'null':
        new_value = new_value.strip("'")
    elif new_value == 'true':
        new_value = new_value.strip("'")
    elif new_value == 'false':
        new_value = new_value.strip("'")
    elif isinstance(new_value, dict):
        new_value = '[complex value]'
    elif isinstance(new_value, str):
        new_value = (f"'{new_value}'")
    return new_value
