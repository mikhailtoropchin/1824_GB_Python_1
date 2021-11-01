class Worker:

    def __init__(self, name, surname, position, income):

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
