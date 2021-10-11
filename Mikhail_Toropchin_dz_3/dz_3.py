def thesaurus(*args):
    result = {}

    [result.setdefault(name[0], args) for name in args]    # создаем словарь, где значение - это весь инпут
    for key, value in result.items():  # убираем лишние слова из значений словаря
        result_list = []
        for val in value:
            if val[0] == key:
                result_list.append(val)
        result[key] = result_list
    # Можно как вариант использовать для сортировки, но результатом будет список кортежей:
    # result = sorted(result.items())

    return result

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Анна"))
