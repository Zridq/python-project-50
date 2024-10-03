from gendiff.formatters.work_with_bool import prepair_value

INDENT = '    '


def unpack(value, deep, buffer=''):
    if value == '':
        buffer = ''
    if isinstance(value, dict):
        for key, value2 in value.items():
            if isinstance(value2, dict):
                buffer += f"\n{INDENT*deep}{key}: {{{unpack(value2, deep+1)}\
\n{INDENT*deep}}}"
            else:
                buffer += f"\n{INDENT*deep}{key}: \
{prepair_value(value2, 'stylish')}"
    else:
        buffer += prepair_value(value, 'stylish')
    return buffer


def make_stylish(diff, lines='{', deep=1):
    for key, value in diff.items():
        if isinstance(value, dict):
            match value['type']:
                case 'nested':
                    lines += f"\n{INDENT*deep}{key}: {{"
                    lines = make_stylish(value['child'], lines, deep + 1)
                case 'added':
                    if isinstance(value['data'], dict):
                        lines += f"\n{INDENT*(deep-1)}  + {key}: {{\
{unpack(value['data'],deep+1)}\n{INDENT*deep}}}"
                        continue
                    lines += f"\n{INDENT*(deep-1)}  + {key}:\
{unpack(value['data'],deep,' ')}"
                case 'notchanged':
                    lines += f"\n{INDENT*(deep)}{key}: \
{prepair_value(value['value1'], 'stylish')}"
                case 'removed':
                    if isinstance(value['data'], dict):
                        lines += f"\n{INDENT*(deep-1)}  - {key}: {{\
{unpack(value['data'],deep+1)}\n{INDENT*deep}}}"
                        continue
                    lines += f"\n{INDENT*(deep-1)}  - {key}:\
{unpack(value['data'],deep, ' ')}"
                case'changed':
                    if isinstance(value['value1'], dict):
                        lines += f"\n{INDENT*(deep-1)}  - {key}: {{\
{unpack(value['value1'],deep + 1)}\n{INDENT*deep}}}"
                    else:
                        lines += f"\n{INDENT*(deep-1)}  - {key}:\
{unpack(value['value1'],deep, ' ')}"
                    if isinstance(value['value2'], dict):
                        lines += f"\n{INDENT*(deep-1)}  + {key}: {{\
{unpack(value['value2'],deep + 1)}\n{INDENT*deep}}}"
                    else:
                        lines += f"\n{INDENT*(deep-1)}  + {key}:\
{unpack(value['value2'],deep, ' ')}"
                case _:
                    lines += f"\n{INDENT*deep}{key}: \
{prepair_value(value, 'stylish')}"
    lines += f"\n{INDENT*(deep - 1)}}}"
    return lines
