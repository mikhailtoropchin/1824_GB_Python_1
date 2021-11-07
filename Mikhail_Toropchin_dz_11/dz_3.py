class ValidateList(Exception):
    _txt = "Введенное значение должно быть числом!"

    def __str__(self):
        return self._txt


some_numbers = []

while True:
    x = input("Введите число для заполнения списка: ")
    if x == "end":
        break
    try:
        if not x.isdigit():
            raise ValidateList
        some_numbers.append(int(x))
    except ValidateList as err:
        print(err)


print(some_numbers)
