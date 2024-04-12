def to_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def get_stylish_format(data, replacer=' ', spases_count=4):  # noqa: C901
    dict_ = ['{']

    def dict_to_str(data, level):
        predicate = replacer * (spases_count * level - 2)
        predicate2 = replacer * spases_count * level
        predicate3 = replacer * spases_count * (level - 1)
        for k, v in data.items():
            v = to_str(v)
            if not isinstance(v, dict):
                if k.startswith(('+ ', '- ', '  ')):
                    dict_.append(f'{predicate}{k}: {v}')
                else:
                    dict_.append(f'{predicate2}{k}: {v}')
            elif isinstance(v, dict):
                if k.startswith(('+ ', '- ', '  ')):
                    dict_.append(f'{predicate}{k}: ' + '{')
                else:
                    dict_.append(f'{predicate2}{k}: ' + '{')
                dict_to_str(v, level + 1)
        dict_.append(f'{predicate3}' + '}')

        return '\n'.join(dict_)

    return dict_to_str(data, 1)
