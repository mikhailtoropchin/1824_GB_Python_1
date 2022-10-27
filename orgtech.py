from exceptions import *

class Department:
    """Класс общий для отделений и подструктур"""
    def __init__(self, name: str, adress: str, purpose: str, staff: str):
        self.name = name
        self.adress = adress
        self.purpose = purpose
        self.staff = staff
        self.items = {"Printer": [], "PC": [], "Laptop": []}


    def move_to_department(self, object, destination):
        """
            переместить предмет в отделение
            :param destination: класс отделение
            :param object: класс (что переносим)
        """
        try:
            if not isinstance(object, Orgtech): # проверяем что отправляем
                raise WrongObject
            if object not in self.items[object.__class__.__name__]: # проверяем есть ли такой объект в отделении
                raise EmptyDep
            else:

                if isinstance(destination, Department): # проверяем куда отправляем
                    destination.items[str(object.__class__.__name__)].append(object)
                    self.items[str(object.__class__.__name__)].remove(object)
                else:
                    raise WrongDest
        except (WrongDest, EmptyDep, WrongObject) as err:
            print(err)


class Warehouse(Department):

    def show_items(self):
        count = 0
        it = {}
        for key, value in self.items.items():
            if len(value) > 0:
                it.setdefault(key, value)
            count += len(value)
        return count, it


class Orgtech:

    all_items = 0

    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def __repr__(self):
        return f"{self.title}"


    def move_to_warehouse(self, destination: Warehouse):
        try:
            if isinstance(destination, Warehouse):
                destination.items[str(self.__class__.__name__)].append(self)
            else:
                raise WrongObject
        except WrongObject as err:
            print(err)


class PC(Orgtech):

    count = 0

    def __init__(self, title: str, price: float, gaming: bool):
        super(PC, self).__init__(title, price)
        self.gaming = gaming
        self.count += 1
        Orgtech.all_items += 1


class Printer(Orgtech):

    count = 0

    def __init__(self, title: str, price: float, multicolor: bool, twosided: bool):
        super(Printer, self).__init__(title, price)
        self.multicolor = multicolor
        self.twosided = twosided
        self.count += 1
        Orgtech.all_items += 1


class Laptop(Orgtech):
    count = 0

    def __init__(self, title: str, price: float, ultra: bool, gaming: bool, battery_time: int):
        super(Laptop, self).__init__(title, price)
        self.ultra = ultra
        self.gaming = gaming
        self.battery_time = battery_time
        self.count += 1
        Orgtech.all_items += 1


HQ = Warehouse("HQ", "some_place", "warehouse", 20)
office = Department("my department", "my place", "office", 1)

# создаем технику
pc = PC("my pc", 100000.0, True)
print(HQ.show_items())

# перемещаем технику на склад
pc.move_to_warehouse(HQ)
print(HQ.show_items())

# перемещаем технику со склада в отдел
HQ.move_to_department(pc, office)
print(office.items)
print(HQ.items)
HQ.move_to_department(pc, office) # проверяем валидацию

HQ.move_to_department("1", office) # проверяем валидацию

