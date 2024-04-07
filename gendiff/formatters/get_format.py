from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json import get_json_format


def get_format(diff, format):
    if format == 'stylish':
        return get_stylish_format(diff)
    elif format == 'plain':
        return get_plain_format(diff)
    elif format == 'json':
        return get_json_format(diff)
    else:
        raise ValueError(f"Формат введен неверно: {format}")
