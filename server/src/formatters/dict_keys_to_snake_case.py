from stringcase import snakecase


def dict_keys_to_snake_case(d: dict) -> dict:
    new_d = {}

    # special case when it is called for element of array being NOT a dict
    if type(d) != dict:
        return d

    for key, value in d.items():
        value = d[key]
        if isinstance(value, dict):
            new_d[snakecase(key)] = dict_keys_to_snake_case(value)
        elif isinstance(value, list):
            new_d[snakecase(key)] = [dict_keys_to_snake_case(v) for v in value]
        else:
            new_d[snakecase(key)] = value

    return new_d
