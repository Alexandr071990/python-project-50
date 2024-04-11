COMMON = '  '
ADD = '+ '
REMOVE = '- '


def get_common(key):
    return f'{COMMON}{key}'


def get_add(key):
    return f'{ADD}{key}'


def get_remove(key):
    return f'{REMOVE}{key}'


def get_diff(dict1, dict2):  # noqa: C901
    result = {}
    sorting = sorted(set(dict1) | set(dict2))
    for key in sorting:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result[get_common(key)] = dict1[key]
            elif dict1[key] != dict2[key]:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):  # noqa: E501
                    result[get_common(key)] = get_diff(
                        dict1[key],
                        dict2[key]
                    )
                else:
                    result[get_remove(key)] = dict1[key]
                    result[get_add(key)] = dict2[key]
        elif key in dict1:
            result[get_remove(key)] = dict1[key]
        elif key in dict2:
            result[get_add(key)] = dict2[key]

    return result
