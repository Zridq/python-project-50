from gendiff.formatters.stylish import make_stylish


def work_with_bool(file):
    bool_list = {True, False}
    for i in file.keys():
        if isinstance(file[i], dict):
            work_with_bool(file[i])
            continue
        if file[i] in bool_list:
            file[i] = str(file[i]).lower()
            continue
        if file[i] is None:
            file[i] = 'null'
    return file


def make_buffer(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    buffer = {}
    for key in keys:
        if key in file1 and key not in file2:
            buffer[key] = {'type': 'removed', 'data': file1[key]}
            continue
        if key not in file1 and key in file2:
            buffer[key] = {'type': 'added', 'data': file2[key]}
            continue
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            child_diff = make_buffer(file1[key], file2[key])
            buffer[key] = {'type': 'nested', 'child': child_diff}
            continue
        elif file1[key] != file2[key]:
            buffer[key] = {
                'type': 'changed',
                'value1': file1[key],
                'value2': file2[key]}
        else:
            buffer[key] = {
                'type': 'notchanged',
                'value1': file1[key]}
    return buffer


def generate_diff(data1, data2, format_name='stylish'):
    file1 = work_with_bool(data1)
    file2 = work_with_bool(data2)
    buffer = make_buffer(file1, file2)
    match format_name:
        case 'stylish':
            result = make_stylish(buffer)
        case _:
            result = 0
    return result
