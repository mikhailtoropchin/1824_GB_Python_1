"""
№2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

from random import randint

arr = []
for i in range(10):
    arr.append(randint(0, 100))

print(arr)


def replace_min_max(arr: list):
    min = arr[0]
    max = 0
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i

    min_ind = arr.index(min)
    max_ind = arr.index(max)
    arr[min_ind], arr[max_ind] = arr[max_ind], arr[min_ind]

    return arr

print(replace_min_max(arr))

