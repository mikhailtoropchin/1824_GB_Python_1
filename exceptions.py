class WrongDate(Exception):
    txt = "Неправльный формат даты"

    def __str__(self):
        return self.txt

class WrongDay(WrongDate):
    txt = "Неправильный день"

class WrongMonth(WrongDate):
    txt = "Неправильный месяц"

class WrongYear(WrongDate):
    txt = "Неправильный год"

# dz_2
class MyZeroDIV(Exception):
    def __str__(self):
        return "На ноль делить нельзя"

#dz_3
class ValidateList(Exception):
    def __str__(self):
        return "Введенное знаение должно быть числом"

class WrongDest(Exception):
    def __str__(self):
        return "Неверный путь отправления!"

class WrongObject(Exception):
    def __str__(self):
        return "Неверный объект!"

class EmptyDep(Exception):
    def __str__(self):
        return "Нет такого объекта!"



# dz complex numbers
class NotComplexNumber(Exception):
    def __str__(self):
        return "Число не комплексное!"

