"""
№2. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.

"""

number = input("Введите число: ")

def rev_num_rec(num: str) -> str:
    if len(num) == 1:
        return num
    return num[-1] + rev_num_rec(num[:-1])

print(rev_num_rec(number))

