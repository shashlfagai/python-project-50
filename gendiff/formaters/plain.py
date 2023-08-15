def plain(diff):
    # Инициализируем отредактированую строку различий
    formatted_diff = formatting_diff(diff)
    # Убираем запятые
    formatted_diff = formatted_diff.replace(',', '')
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
            if 'new_value' in v or 'old_value' in v:
                formatted_diff = formatting_diff_of_flat_dict(
                    k, v, formatted_diff, way
                    )
            else:
                nested_value = formatting_diff(v, way + f'{k}.')
                formatted_diff += nested_value
    return formatted_diff


def formatting_diff_of_flat_dict(k, v, formatted_diff, way):
    way += k
    old_value = formatting_old_value(v['old_value'])
    new_value = formatting_new_value(v['new_value'])
    if v["new_value"] == 'not_for_add_to_dict':
        formatted_diff += (f"Property '{way}' was removed\n")
    elif v['old_value'] == 'not_for_add_to_dict':
        formatted_diff += (
            f"Property '{way}' was added with value: "
            f"{new_value}\n"
            )
    else:
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
