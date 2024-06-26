def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    return f"'{value}'"


def get_plain_path(path):
    separator = '.'
    return separator.join(path)


def message_plain(path, value1, value2):
    path = get_plain_path(path)
    value1 = to_str(value1)
    value2 = to_str(value2)

    added = f"Property '{path}' was added with value: {value1}"
    removed = f"Property '{path}' was removed"
    updated = f"Property '{path}' was updated. From {value1} to {value2}"
    return {'added': added, 'removed': removed, 'updated': updated}


def get_added(message):
    return message['added']


def get_removed(message):
    return message['removed']


def get_updated(message):
    return message['updated']


def get_plain_format(data):  # noqa C901
    result = []

    def dict_to_str(data, start_path=[]):
        for key, val in data.items():
            orig_key = key[len(ADD):]
            path = start_path + [orig_key]
            messages = message_plain(path, val, data.get(f"+ {orig_key}"))

            if key.startswith(COMMON) and isinstance(val, dict):
                dict_to_str(val, path)
            elif key.startswith(REMOVE) and f"{ADD}{orig_key}" in data:
                result.append(get_updated(messages))
            elif key.startswith(REMOVE) and f"{ADD}{orig_key}" not in data:
                result.append(get_removed(messages))
            elif key.startswith(ADD) and f"{REMOVE}{orig_key}" not in data:
                result.append(get_added(messages))

        return '\n'.join(result)

    return dict_to_str(data)
