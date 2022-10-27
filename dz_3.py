from exceptions import ValidateList

some_list = []
while True:
    val = input("Введите число, либо q - чтобы выйти: ")
    if val == "q":
        break
    try:
        if not val.isdigit():
            raise ValidateList
        some_list.append(int(val))
    except ValidateList as err:
        print(err)

print(some_list)

