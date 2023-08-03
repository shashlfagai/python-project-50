import json
import yaml


def parsing_data(file_path):
    # Открываем файлы и загружаем их содержимое в словари
    with open(file_path) as file:
        path_name = file_path
        # Определяем формат файла и загружаем данные
        if path_name.endswith(".json"):
            data = json.load(file)
        elif path_name.endswith(".yml") or path_name.endswith(".yaml"):
            data = yaml.safe_load(file)
        data = convert_to_lowercase(data)
        return data


def convert_to_lowercase(data):
    if isinstance(data, dict):
        return {key.lower(): convert_to_lowercase(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_lowercase(item) for item in data]
    elif isinstance(data, str):
        return data.lower()
    else:
        return data
