"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и округление до целого числа деления клеток соответственно.
"""

class Cell:
    def __init__(self, num_of_cells: int):
        self.cells = num_of_cells

    def __str__(self):
        return f"клетка с количеством ячеек {self.cells}"

    #сложение двух клеток
    def __add__(self, other):
        result = self.cells + other.cells
        return Cell(result)

    # вычитание двух клеток (если разность больше 0)
    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            raise TypeError("слишком мало ячеек в исходной клетке")

    # умножение двух клеток
    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    # целочисленное деление двух клеток
    def __floordiv__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells // other.cells)
        else:
            raise TypeError("слишком мало ячеек в исходной клетке")

    # упорядочить клетки
    def make_order(self, num: int):
        if num and isinstance(num, int): # проверяем на всякий случай, чтобы аргумент был > 0 и инт.
            im = self.cells // num # целочисленное деление
            end = self.cells % num # остаток от деления (для последней строки)
            return f"{'*' * num}\n" * im + "*" * end
        else:
            raise TypeError("аргументом должно быть целое цисло больше нуля")

prokaryotes = Cell(9)
eukaryotes = Cell(15)
print("Выполняем сложение двух клеток, результат: ")
print(prokaryotes + eukaryotes)
print("\nВыполняем вычитание двух клеток, результат: ")
print(eukaryotes - prokaryotes)
print("\nВыполняем умножение двух клеток, результат: ")
print(eukaryotes * prokaryotes)
print("\nВыполняем целочисенное деление двух клеток, результат: ")
print(eukaryotes // prokaryotes)
print("\nОрганизовываем порядок ячеек в клетке: ")
print(eukaryotes.make_order(9))

