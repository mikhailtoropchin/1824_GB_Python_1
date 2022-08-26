"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""
class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["Wage"] + self._income["Bonus"]


miha = Position("Mikhail", "Toropchin", "boss", {"Wage": 100, "Bonus": 12})
print(miha.position)
print(miha.name)
print(miha.surname)
print(miha._income)
print(miha.get_full_name())
print(miha.get_total_income())

