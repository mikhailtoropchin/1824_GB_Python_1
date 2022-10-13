"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title


    def __str__(self):
        return f"класс {self.__class__.__name__}"

    # сложение общих затрат разных видов одежды (по два)
    def __add__(self, other):
        return self.calc_exp + other.calc_exp # благодаря @property можно без скобок (метод как аттрибут)

    @abstractmethod # абстрактный метод (должен быть у каждого чайлда)
    def calc_exp(self):
        pass


class Coat(Clothes):
    def __init__(self, title, size):
        super(Coat, self).__init__(title)
        self.size = size

    @property
    def calc_exp(self):
        return (self.size/6.5) + 0.5


class Suit(Clothes):
    def __init__(self, title, height):
        super(Suit, self).__init__(title)
        self.height = height

    @property
    def calc_exp(self):
        return (2 * self.height) + 0.3


suit = Suit("костюм", 100)
print(suit)
print(f"затраты ткани на {suit.title} - {suit.calc_exp}")
coat = Coat("пальто", 120)
print(coat)
print(f"затраты ткани на {coat.title} - {coat.calc_exp}")
print(f"общие затраты: {suit + coat}")

