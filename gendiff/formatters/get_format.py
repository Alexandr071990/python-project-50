from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_formatter


def get_format(diff, format):
    if format == 'stylish':
        return stylish(diff)
    elif format == 'plain':
        return plain(diff)
    elif format == 'json':
        return get_json_formatter(diff)
    else:
        raise ValueError(f"Формат введен неверно: {format}")
