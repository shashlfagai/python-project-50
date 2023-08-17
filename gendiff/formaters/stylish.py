def stylishing(diff):
    # Инициализируем отредактированую строку различий
    formatted_diff = formating_inner_diff(diff, depth=1)
    # Открываем и закрываем вложенности
    formatted_diff = '{\n' + formating_inner_diff(diff)
    formatted_diff += "}"
    # Убираем запятые
    formatted_diff = formatted_diff.replace(',', '')
    return formatted_diff


def formating_inner_diff(diff, depth=1):
    # Создаем строку для хранения отформатированных различий
    formatting_diff = ''
    # Определяем отступы для каждого уровня вложенности
    deep_indent = '    ' * depth
    deep_indent_minus = deep_indent[:-2] + '- '
    deep_indent_plus = deep_indent[:-2] + '+ '
    # Перебираем различия и форматируем каждую пару ключ-значение
    # в зависимости от того новое это значение или старое, или не измененное
    for key, value in diff.items():
        if not isinstance(value, dict):
            # Если значение не словарь, добавляем его к отформатированной строке
            formatting_diff += f'{deep_indent}{key}: {value}\n'
        else:
            # Если значение словарь, рекурсивно форматируем его
            formatting_diff = formating_diff_of_value(
                key, value, formatting_diff,
                deep_indent, deep_indent_plus, deep_indent_minus,
                depth
            )
    return formatting_diff


def formating_diff_of_value(
        key, value, formatting_diff,
        deep_indent, deep_indent_plus, deep_indent_minus,
        depth):
    if 'new_value' not in value and 'old_value' not in value:
        # Если вложенные значения отсутствуют,
        # добавляем ключ и значение как есть
        nested_diff = formating_inner_diff(value, depth + 1)
        formatting_diff += (
            f'{deep_indent}{key}: {{\n'
            f'{nested_diff}{deep_indent}}},\n'
        )
    elif value['old_value'] == 'not_for_add_to_dict':
        # Если значение было добавлено (новое), форматируем как "добавление"
        formatting_diff = formating_diff_with_new_value(
            key, value, formatting_diff,
            deep_indent, deep_indent_plus,
            depth
        )
    elif value['new_value'] == 'not_for_add_to_dict':
        # Если значение было удалено, форматируем как "удаление"
        formatting_diff = formating_diff_with_old_value(
            key, value, formatting_diff,
            deep_indent, deep_indent_minus,
            depth
        )
    else:
        # Если значение было изменено, форматируем как "изменение"
        formatting_diff = formating_diff_with_old_and_new_values(
            key, value, formatting_diff,
            deep_indent, deep_indent_plus, deep_indent_minus,
            depth
        )
    return formatting_diff


def formating_diff_with_old_and_new_values(
        key, value, formatting_diff,
        deep_indent, deep_indent_plus, deep_indent_minus,
        depth):
    new_value = value['new_value']
    old_value = value['old_value']
    # Форматируем значения, если одно словарь, а другое - простое значение
    if not isinstance(new_value, dict) and isinstance(old_value, dict):
        nested_diff = formating_inner_diff(old_value, depth + 1)
        formatting_diff += (
            f'{deep_indent_minus}{key}: {{\n'
            f'{nested_diff}{deep_indent}}}\n'
        )
        formatting_diff += f'{deep_indent_plus}{key}: {new_value}\n'
    elif not isinstance(old_value, dict) and isinstance(new_value, dict):
        nested_diff = formating_inner_diff(new_value, depth + 1)
        formatting_diff += f'{deep_indent_minus}{key}: {old_value}\n'
        formatting_diff += (
            f'{deep_indent_plus}{key}: {{\n'
            f'{nested_diff}{deep_indent}}}\n'
        )
    # Форматируем значения, если оба значения простые
    elif not isinstance(old_value, dict) and not isinstance(new_value, dict):
        formatting_diff += f'{deep_indent_minus}{key}: {old_value}\n'
        formatting_diff += f'{deep_indent_plus}{key}: {new_value}\n'
    else:
        nested_old_diff = formating_inner_diff(old_value, depth + 1)
        nested_new_diff = formating_inner_diff(new_value, depth + 1)
        formatting_diff += (
            f'{deep_indent_minus}{key}: {{\n'
            f'{nested_old_diff}{deep_indent}}}\n'
        )
        formatting_diff += (
            f'{deep_indent_plus}{key}: {{\n'
            f'{nested_new_diff}{deep_indent}}}\n'
        )
    return formatting_diff


def formating_diff_with_new_value(
        key, value, formatting_diff,
        deep_indent, deep_indent_plus,
        depth):
    if not isinstance(value['new_value'], dict):
        formatting_diff += f'{deep_indent_plus}{key}: {value["new_value"]}\n'
    elif isinstance(value['new_value'], dict):
        nested_diff = formating_inner_diff(value['new_value'], depth + 1)
        formatting_diff += (
            f'{deep_indent_plus}{key}: {{\n'
            f'{nested_diff}{deep_indent}}}\n'
        )
    return formatting_diff


def formating_diff_with_old_value(
        key, value, formatting_diff,
        deep_indent, deep_indent_minus,
        depth):
    if not isinstance(value['old_value'], dict):
        formatting_diff += f'{deep_indent_minus}{key}: {value["old_value"]}\n'
    elif isinstance(value['old_value'], dict):
        nested_diff = formating_inner_diff(value['old_value'], depth + 1)
        formatting_diff += (
            f'{deep_indent_minus}{key}: {{\n'
            f'{nested_diff}{deep_indent}}}\n'
        )
    return formatting_diff
