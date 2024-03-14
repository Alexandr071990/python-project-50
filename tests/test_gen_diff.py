from gendiff.generate_diff import generate_diff
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
    recurse_yml_path1 = get_fixture_path('recurse_file1.yaml')
    recurse_yml_path2 = get_fixture_path('recurse_file2.yaml')
    recurse_json_path1 = get_fixture_path('recurse_file1.json')
    recurse_json_path2 = get_fixture_path('recurse_file2.json')

    correct_result_json = read(get_fixture_path('expected_results.txt'))
    correct_recurse_result = read(get_fixture_path('recurse_result.txt'))

    result_with_json = generate_diff(json_path1, json_path2)
    result_with_yml = generate_diff(yml_path1, yml_path2)
    recurse_result_with_json = generate_diff(recurse_json_path1, recurse_json_path2)
    recurse_result_with_yml = generate_diff(recurse_yml_path1, recurse_yml_path2)


    assert result_with_json == correct_result_json
    assert result_with_yml == correct_result_json
    assert recurse_result_with_json == correct_recurse_result
    assert recurse_result_with_yml == correct_recurse_result
    