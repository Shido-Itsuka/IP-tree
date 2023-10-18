import json

number = [4096, 2048, 1024]


# Рекурсивная функция для создания словаря
def create_nested_dict(number, count):
    if count == 0:
        return {}
    next_number = number[1:]
    nested_dict = {
        number[0]: (create_nested_dict(next_number, count - 1), create_nested_dict(next_number, count - 1))
    }

    return nested_dict


# Создание словаря
dictionary = {
    number[0]: (create_nested_dict(number[1:], len(number)-1), create_nested_dict(number[1:], len(number)-1))
}


def get_all_keys(dictionary):
    keys = []
    for key, value in dictionary.items():
        keys.append(key)
        if isinstance(value, tuple):
            for nested_dict in value:
                keys.extend(get_all_keys(nested_dict))
    return keys


# Вывод словаря
print(json.dumps(dictionary, indent=2))
print(dictionary, sorted(list(get_all_keys(dictionary)), reverse=True), sep='\n\n')
zxc = {
}
