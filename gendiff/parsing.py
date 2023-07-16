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
        return data
