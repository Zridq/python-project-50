import json
import os
import yaml


def get_file_format(file_name):
    _, file_extension = os.path.splitext(file_name)
    return file_extension


def get_file_concent(file_name):
    with open(file_name) as f:
        content = f.read()
    return content


def get_file(content, extension):
    if extension == 'yaml' or 'yml':
        return (yaml.safe_load(content))
    if extension == 'json':
        return (json.load(content))
    else:
        raise ValueError(f'Unsupported extension {extension}')


def parse_file(file):
    content = get_file_concent(file)
    extension = get_file_format(file)
    parse_result = get_file(content, extension)
    return (parse_result)
