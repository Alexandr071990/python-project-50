import json


def get_json_formatter(data):
    return json.dumps(data, indent=4)
