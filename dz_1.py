"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def div_numbers(num_1, num_2):
    result = ""
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
    return result

print(div_numbers(int(input("Первое число: ")), int(input("Второе число: "))))

