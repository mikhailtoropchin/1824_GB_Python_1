"""
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

"""

my_list = [7, 5, 3, 3, 2]

while True:
    new_digit = input("Цифру сюда: ")

    if new_digit == "q":
        break

    new_digit = int(new_digit)
    for ind, dig in enumerate(my_list):
        if dig < new_digit:
            my_list.insert(ind, new_digit)
            print(my_list)
            break
        if dig == new_digit:
            my_list.insert(ind + 1, new_digit)
            print(my_list)
            break
        if dig > new_digit:
            if ind == len(my_list) - 1:
                my_list.append(new_digit)
                print(my_list)
                break
            else:
                continue

