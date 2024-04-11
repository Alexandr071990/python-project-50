import pytest

from gendiff import generate_diff
from tests import get_path


@pytest.mark.parametrize(
    'path_to_file1, path_to_file2, formatter, expected',
    [
        (
            'recurse_file1.json',
            'recurse_file2.json',
            'stylish',
            'result_stylish.txt'
        ),
        (
            'recurse_file1.yaml',
            'recurse_file2.yaml',
            'stylish',
            'result_stylish.txt'
        ),
        (
            'recurse_file1.json',
            'recurse_file2.json',
            'plain',
            'result_plain.txt'
        ),
        (
            'recurse_file1.yaml',
            'recurse_file2.yaml',
            'plain',
            'result_plain.txt'
        ),
        (
            'recurse_file1.json',
            'recurse_file2.json',
            'json',
            'result_json.txt'
        ),
        (
            'recurse_file1.yaml',
            'recurse_file2.yaml',
            'json',
            'result_json.txt'
        )
    ]
)
def test_gendiff(path_to_file1, path_to_file2, formatter, expected):
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result_data = file.read()
    test_path1 = get_path(path_to_file1)
    test_path2 = get_path(path_to_file2)
    assert generate_diff(test_path1, test_path2, formatter) == result_data
