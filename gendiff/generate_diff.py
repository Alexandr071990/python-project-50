from gendiff.parser import get_data
from gendiff.data_parser import get_diff
from gendiff.formatters.get_format import get_format


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = get_data(file_path1)
    dict2 = get_data(file_path2)
    diff = get_diff(dict1, dict2)

    return get_format(diff, format)
