class WrongObject(Exception):
    def __str__(self):
        return "Оргтехнику нужно отправлять на склад!"

class WrongDestination(Exception):
    def __str__(self):
        return "Со склада техника должна отправляться в отделения!"

class WarehouseEmpty(Exception):
    def __str__(self):
        return "Предмета нет на складе!"



class NotComplexNumber(Exception):
    def __str__(self):
        return "Числа для операции должны быть комплексными!"



class WrongDate(Exception):
    txt = "Неправильный формат даты"
    add = ""


    def __init__(self, num=None):
        if num:
            self.add = num


    def __str__(self):
        return f"{self.txt} {self.add}"


class WrongDay(WrongDate):
    txt = "Неправильный день"


class WrongMonth(WrongDate):
    txt = "Неправильный месяц"


class WrongYear(WrongDate):
    txt = "Неправильный год"