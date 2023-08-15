import json
import yaml


def parsing_data(file_path):
    # Открываем файлы и загружаем их содержимое в словари
    with open(file_path) as file:
        path_name = file_path
        # Определяем формат файла и загружаем данные
        if path_name.endswith(".json"):
            # Если формат файла JSON, читаем его содержимое
            json_string = file.read()
            # Заменяем значение "null" на строку '"null"'
            json_string_with_null = json_string.replace('null', '"null"')
            # Загружаем данные в словарь
            data = json.loads(json_string_with_null)
        elif path_name.endswith(".yml") or path_name.endswith(".yaml"):
            # Если формат файла YAML,
            # Читаем содержимое файла
            yaml_string = file.read()
            # Заменяем значение "null" на строку '"null"'
            yaml_string_with_null = yaml_string.replace('null', '"null"')
            # загружаем данные с помощью библиотеки PyYAML
            data = yaml.safe_load(yaml_string_with_null)
        # Возвращаем данные
        return data
