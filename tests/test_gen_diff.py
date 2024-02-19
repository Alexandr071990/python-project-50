from gendiff.gen_diff import generate_diff
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

def test_gen_diff():
    yml_path1 = get_fixture_path('file1.yml')
    yml_path2 = get_fixture_path('file2.yml')
    json_path1 = get_fixture_path('file1.json')
    json_path2 = get_fixture_path('file2.json')
    correct_result = read(get_fixture_path('expected_results.txt'))
    func_result_with_json = generate_diff(json_path1, json_path2)
    func_result_with_yml = generate_diff(yml_path1, yml_path2)

    assert func_result_with_json == correct_result
    assert func_result_with_yml == correct_result
    
