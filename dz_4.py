"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
"""
def num_degrees(x, y):
    mult_num = x
    count = 1
    while count < abs(y):
        mult_num = x * mult_num
        count += 1
    result = 1 / (mult_num)
    return result

print(num_degrees(5, -4))


def my_func_easy(x, y):
    return x ** y

print(my_func_easy(5, -4))

