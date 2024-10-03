from gendiff.formatters.work_with_bool import prepair_value


def make_plain(diff, lines="", buffer="", first=True, first_enter=True):
    for key, value in diff.items():
        if first_enter is True:
            first_enter = False
        else:
            lines += "\n"
        if isinstance(value, dict):
            if first is True:
                buffer = f"'{key}"
            match value['type']:
                case 'nested':
                    if first is False:
                        lines = make_plain(value['child'], lines,
                                           (buffer + f".{key}"), False, True)
                    else:
                        lines = make_plain(value['child'], lines,
                                           buffer, False, True)
                case 'added':
                    if first:
                        lines += f"Property '{key}' was added with value: "
                    else:
                        lines += f"Property {buffer}.{key}' \
was added with value: "
                    if isinstance(value['data'], dict):
                        lines += "[complex value]"
                        continue
                    lines += f"{prepair_value(value['data'], 'plain')}"
                case 'removed':
                    if first:
                        lines += f"Property '{key}' was removed"
                    else:
                        lines += f"Property {buffer}.{key}' was removed"
                    continue
                case'changed':
                    if first:
                        lines += f"Property '{key}' was updated. From "
                    else:
                        lines += f"Property {buffer}.{key}' was updated. From "
                    if isinstance(value['value1'], dict):
                        lines += "[complex value]"
                    else:
                        lines += f"{prepair_value(value['value1'], 'plain')}"
                    if isinstance(value['value2'], dict):
                        lines += "[complex value]"
                    else:
                        lines += f" to \
{prepair_value(value['value2'], 'plain')}"
                case'notchanged':
                    first_enter = True
                case _:
                    continue
    return lines
