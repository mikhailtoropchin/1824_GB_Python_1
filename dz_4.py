"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
   Для решения используйте цикл while и арифметические операции.
"""

some_number = int(input("Введите число: "))
n = 0
while some_number:
    res = some_number % 10
    if res > n:
        n = res
    some_number = some_number // 10
print(n)

