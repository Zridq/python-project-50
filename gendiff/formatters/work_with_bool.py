def prepair_value(value, type):
    print(value)
    bool_list = {True, False}
    if value in bool_list:
        value = f"{str(value).lower()}"
        return value
    if value is None:
        value = 'null'
        return value
    else:
        if type == 'stylish':
            value = f"{value}"
            return value
        if type == 'plain':
            value = f"'{value}'"
    return value
