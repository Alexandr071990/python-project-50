import json


def generate_diff(filepath1, filepath2):

    data1 = json.load(open(filepath1))
    data2 = json.load(open(filepath2))

    keys = list(set(list(data1.keys()) + list(data2.keys())))
    keys.sort()

    def to_str(data):
        data_str = {}
        for key in data.keys():
            data_str[key] = str(data[key])
        return data_str

    data1_str = to_str(data1)
    data2_str = to_str(data2)

    result = '{\n'
    for key in keys:
        if key in data1_str:
            if key in data2_str:
                if data1_str[key] == data2_str[key]:
                    result += f'    {key}: {data1_str[key]}\n'
                else:
                    result += f'  - {key}: {data1_str[key]}\n  + {key}: {data2_str[key]}\n'
            else:
                result += f'  - {key}: {data1_str[key]}\n'
        else:
            result += f'  + {key}: {data2_str[key]}\n'
    result += '}'

    return result