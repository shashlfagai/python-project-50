import json
import yaml


def parsing_data1(file1_path):
    # Открываем файлы и загружаем их содержимое в словари
    with open(file1_path) as file1:
        path_name1 = file1_path
        # Определяем формат файла и загружаем данные
        if path_name1.endswith(".json"):
            data1 = json.load(file1)
        elif path_name1.endswith(".yml") or path_name1.endswith(".yaml"):
            data1 = yaml.safe_load(file1)
        return data1


def parsing_data2(file2_path):
    # Открываем файлы и загружаем их содержимое в словари
    with open(file2_path) as file2:
        path_name2 = file2_path
        # Определяем формат файла и загружаем данные
        if path_name2.endswith(".json"):
            data2 = json.load(file2)
        elif path_name2.endswith(".yml") or path_name2.endswith(".yaml"):
            data2 = yaml.safe_load(file2)
        return data2
