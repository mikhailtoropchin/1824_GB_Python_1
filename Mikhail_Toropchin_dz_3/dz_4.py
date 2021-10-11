def thesaurus(*args):
    result = {}

    for name in args:
        result.setdefault(name[0], args)

    for key, value in result.items():
        result_list = []
        for val in value:
            if val[0] == key:
                result_list.append(val)
        result[key] = result_list

    return result


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
