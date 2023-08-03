import os


from gendiff.gendiff_func import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


file1_json_data = get_fixture_path('file1.json')
file2_json_data = get_fixture_path('file2.json')
file1_yml_data = get_fixture_path('file1.yml')
file2_yml_data = get_fixture_path('file2.yml')
file1_deep_json_data = get_fixture_path('file1deep.json')
file2_deep_json_data = get_fixture_path('file2deep.json')


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
    assert generate_diff(file1_path, file2_path) == expected_result


def test_gendiff_deep_josn():
    file1_path = file1_deep_json_data
    file2_path = file2_deep_json_data
    expected_result = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    assert generate_diff(file1_path, file2_path) == expected_result