"""
№6. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

"""
# Вводимые данные:
numbers = input("Введите последовательность чисел через пробел").split(" ")


# Решение через строку
def find_max_of_dig(arr: list) -> tuple:
    max = 0
    n = 0
    for n in arr:
        res = 0
        for i in n:
            res += int(i)
        if res > max:
            max = res
            n = int(n)
    return max, n



sum, num = find_max_of_dig(numbers)
print(f"Число - {num}, сумма его цифр - {sum}.")



# Решение мат.
def find_max_mat(arr: list) -> tuple:
    max = 0
    n = 0
    for x in [int(i) for i in arr]:
        res = 0
        y = x
        while y > 0:
            res += y % 10
            y = y // 10
        if res > max:
            max = res
            n = x
    return max, n

sum, num = find_max_mat(numbers)
print(f"Число - {num}, сумма его цифр - {sum}.")

