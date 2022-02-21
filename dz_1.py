"""
№1. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""

number = input("Введите число: ")
count_even = 0
count_odd = 0
for n in number:
    if int(n) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Четные цифры: {count_even}")
print(f"Нечетные цифры: {count_odd}")

