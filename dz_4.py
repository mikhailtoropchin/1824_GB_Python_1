""" 4. Написать программу, которая генерирует в указанных пользователем границах:
        случайное целое число;
        случайное вещественное число;
        случайный символ.
        Для каждого из трех случаев пользователь задает свои границы диапазона.
        Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
        Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

request = input("1. Выбрать случайное число \n2. Выбрать случайное вещественное число\n3. Выбрать случайный символ. ")
user_range_1, user_range_2 = input("Диапазон/символ от: "), input("до: ")

def get_random_stuff(r: str, u_range_1: int, u_range_2: int):
    if r.isdigit():
        if int(r) in (1, 2):
            if u_range_1.isdigit() and u_range_2.isdigit():
                u_range_1, u_range_2 = int(u_range_1), int(u_range_2)
                if int(r) == 1:
                    return random.randint(u_range_1, u_range_2)
                else:
                    return random.uniform(u_range_1, u_range_2)
            else:
                return "Нужно ввести числа диапазона"
        elif int(r) == 3:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            if not u_range_1.isdigit() and not u_range_2.isdigit():
                if u_range_1 in alphabet and u_range_2 in alphabet:
                    if ord(u_range_1) < ord(u_range_2):
                        return chr(random.randint(ord(u_range_1), ord(u_range_2)))
                    else:
                        return chr(random.randint(ord(u_range_2), ord(u_range_1)))
                else:
                    return "Нужно ввести буквы алфавита"
            else:
                return "Нужно ввести буквы алфавита"
        else:
            return "Нужно выбрать один из трех вариантов."
    else:
        return "Нужно выбрать один из трех вариантов."

print(get_random_stuff(request, user_range_1, user_range_2))

#---------------------------------------------------------------------------------------------------------------

