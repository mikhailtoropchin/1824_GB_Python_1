"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе
"""
my_list = [23, True, "one", [1, 0], ("d", 12), {1, 3, 5, False}, {1: "one", 2: "two"}]

for i in my_list:
    print(type(i))

