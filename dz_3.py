"""
№3. В одномерном массиве найти сумму элементов,
   находящихся между минимальным и максимальным элементами.
   Сами минимальный и максимальный элементы в сумму не включать.

"""

from random import randint

arr = []
for i in range(10):
    arr.append(randint(0, 100))

print(arr)


def sum_min_max(arr: list):
    min = arr[0]
    max = 0
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    sum = 0
    min_ind = arr.index(min)
    max_ind = arr.index(max)

    if min_ind > max_ind:
        min_ind, max_ind = max_ind, min_ind

    for i in arr[min_ind + 1:max_ind]:
        sum += i

    return sum

print(sum_min_max(arr))

