from pathlib import Path
import json
import yaml


def get_data(file_path):
    with open(file_path, "r") as data:
        return parse(data.read(), Path(file_path).suffix[1:])


def parse(data, format: str):
    if format == 'json':
        return json.loads(data)
    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(data)
    raise Exception(f"No such method for format: {format}")
