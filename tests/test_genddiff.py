from gendiff.gendiff_func import generate_diff

def test_gendiff():
    file1_path = 'files/file1.json'
    file2_path = 'files/file2.json'
    expected_result = '''{
 - follow: False
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: True
}'''
    assert generate_diff(file1_path, file2_path) == expected_result
