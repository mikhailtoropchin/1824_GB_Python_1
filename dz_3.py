"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
   Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
num_to_sum = input("Введите число: ")
print(int(num_to_sum) + int(num_to_sum * 2) + int(num_to_sum * 3))

