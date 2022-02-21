# №3. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
#     Количество элементов (n) вводится с клавиатуры.

num = int(input("Введите число: "))

def sum_num(n):
    sum = 0
    x = 1
    for i in range(n):
        sum += x
        x = x / -2
    return sum

print(sum_num(num))

# Решение через рекурсию (слишком долго работает):

def sum_num_rec(n: int) -> bool:
    def helper(n: int):
        if n < 2:
            return n
        result = helper(n-2) / 2 - helper(n - 1) / -2
        return result
    return helper(n)

# print(sum_num_rec(3))

