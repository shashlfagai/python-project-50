import os
import json


from gendiff.gendiff_func import generate_diff
# from gendiff.formaters.stylish import stylishing
# from gendiff.formaters.plain import plain
# from gendiff.formaters.jsonutils import serializing


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


file1_json_data = get_fixture_path('file1.json')
file2_json_data = get_fixture_path('file2.json')
file1_yml_data = get_fixture_path('file1.yml')
file2_yml_data = get_fixture_path('file2.yml')
file1_deep_json_data = get_fixture_path('file1deep.json')
file2_deep_json_data = get_fixture_path('file2deep.json')
# diff_of_flat_files_result = get_fixture_path('diff_flat_files_result.json')
diff_of_deep_files_result = get_fixture_path('diff_deep_files_result.json')


def test_gendiff_json():
    file1_path = file1_json_data
    file2_path = file2_json_data
    expected_result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(file1_path, file2_path) == expected_result


def test_gendiff_yml():
    file1_path = file1_yml_data
    file2_path = file2_yml_data
    expected_result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(file1_path, file2_path, 'stylish') == expected_result


def test_gendiff_deep_josn():
    file1_path = file1_deep_json_data
    file2_path = file2_deep_json_data
    with open(diff_of_deep_files_result) as expected_file:
        expected_result = expected_file.read()
    assert generate_diff(file1_path, file2_path, 'stylish') == expected_result


def test_gendiff_deep_josn_plain():
    file1_path = file1_deep_json_data
    file2_path = file2_deep_json_data
    expected_result = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''
    assert generate_diff(file1_path, file2_path, 'plain') == expected_result


def test_gendiff_flat_josn_plain_():
    file1_path = file1_json_data
    file2_path = file2_json_data
    expected_result = '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''
    assert generate_diff(file1_path, file2_path, 'plain') == expected_result


def test_gendiff_json_format():
    # Подготавливаем пути к файлам
    file1_path = file1_json_data
    file2_path = file2_json_data
    # Вызываем функцию generate_diff для получения результата
    result = generate_diff(file1_path, file2_path, 'json')
    # Загружаем JSON-объект из результата
    try:
        parsed_result = json.loads(result)
    except json.JSONDecodeError:
        # Если не удалось распарсить JSON, тест провален
        assert False, "Failed to parse the generated JSON"
    # Проверяем, что парсированный результат является словарем или списком (валидным JSON)
    assert isinstance(parsed_result, (dict, list)), "Generated JSON is not a valid object"
    # Если тест успешно дошел до этой точки, значит JSON возвращается корректно
    assert True

