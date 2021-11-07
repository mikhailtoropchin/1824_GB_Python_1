from exceptions import WrongObject, WrongDestination, WarehouseEmpty
from departments import Departments, DepartmentOfMystery

class Warehouse:
    """Класс для хранения всех оргтехники"""

    def __init__(self, name: str, it=None):
        self.name = name
        self.items = {"Printer": [], "Scaner": [], "Xerox": []}
        if it:
            self.items = it


    def show_items(self, title: str=None):
        """показывает технику на складе в данный момент, где title - если нужно посмотрть конкретный тип техники"""
        if title: # если нужно показать отдельную группу
            print(f"На складе {self.name} в данный момент:")
            print(f"{title}'ов: {len(self.items[title])} штук")
        else: # дефолтный показ всех
            print(f"На складе {self.name} в данный момент:")
            print(f"Принтеров: {len(self.items['Printer'])} штук")
            print(f"Сканеров: {len(self.items['Scaner'])} штук")
            print(f"Ксероксов: {len(self.items['Xerox'])} штук")


    def move_item(self, item, destination):
        """
        переместить предмет в отделение
        :param destination: класс отделение
        :param item: класс (предмет, который хранится на складе)
        """
        try:
            #проверка наличия перемещаемого предмета на складе
            if item not in self.items[item.__class__.__name__]:
                raise WarehouseEmpty
            else:
                # валидация по наследованию (все отделения - наследники класса Departments)
                if issubclass(destination.__class__, Departments):
                    if str(item.__class__.__name__) in destination.items.keys():
                        self.items[str(item.__class__.__name__)].remove(item)
                        destination.items[str(item.__class__.__name__)].append(item)
                        print(f"{item.__class__.__name__} {item.title} был перемещен в отделение {destination.title}")
                    else: # нужно создать лист, если в ключах нет названия класса
                        destination.items[str(item.__class__.__name__)] = []
                        destination.items[str(item.__class__.__name__)].append(item)
                        self.items[str(item.__class__.__name__)].remove(item)
                        print(f"{item.__class__.__name__} {item.title} был перемещен в отделение {destination.title}")
                else:
                    raise WrongDestination
        except (WrongDestination, WarehouseEmpty) as err:
            print(err)


class Orgtech:
    """Шаблон для оргтехники"""
    all_tech = 0 # счетчик всей оргтехники (обновляется при создании экземпляра наследника)

    def __init__(self, title, price):
        self.title = title
        self.price = price


    def move_to_warehouse(self, where):
        """Переместить предмет на склад"""
        try:
            if isinstance(where, Warehouse):
                where.items[str(self.__class__.__name__)].append(self)
            else:
                raise WrongObject
        except WrongObject as err:
            print(err)

    @classmethod
    def show_all(cls):
        print(f"Всего оргтехники в корпорации: {Orgtech.all_tech}")


class Printer(Orgtech):
    count = 0
    def __init__(self, title: str, price: float, multicolor: bool, scan_included: bool):
        super(Printer, self).__init__(title, price)
        self.color = multicolor
        self.scan = scan_included
        self.count += 1
        Orgtech.all_tech += 1


class Scaner(Orgtech):
    count = 0
    def __init__(self, title, price, can_copy):
        super(Scaner, self).__init__(title, price)
        self.copy = can_copy
        self.count += 1
        Orgtech.all_tech += 1


class Xerox(Orgtech):
    count = 0
    def __init__(self, title, price, can_scan):
        super(Xerox, self).__init__(title, price)
        self.can_scan = can_scan
        self.count += 1
        Orgtech.all_tech += 1

# определяем классы для проверки работы
hp = Printer("HP", 100, True, True)
ultra_print = Printer("Ultra", 400, True, True)
canon = Scaner("Canon", 150, True)
old = Xerox("Old", 20, False)
storage = Warehouse("storage")
mystery = DepartmentOfMystery("Mystery")

#пробуем разные методы
hp.move_to_warehouse(storage)
ultra_print.move_to_warehouse(storage)
storage.show_items()

storage.move_item(ultra_print, mystery)
storage.move_item(hp, mystery)
mystery.show_items()

Orgtech.show_all()
