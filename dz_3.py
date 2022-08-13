"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""
from random import randint

def my_func(num_1, num_2, num_3):
    max_1 = 0
    max_2 = 0
    for num in num_1, num_2, num_3:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2:
            max_2 = num
    print(num_1, num_2, num_3)
    return max_1 + max_2

print(f"Сумма наибольших двух чисел: {my_func(randint(0, 100), randint(0, 100), randint(0, 100))}")

