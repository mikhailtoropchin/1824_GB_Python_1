"""
№4. В одномерном массиве целых чисел определить два наименьших элемента.
   Они могут быть как равны между собой (оба являться минимальными), так и различаться.

"""
from random import randint

arr = []
for i in range(10):
    arr.append(randint(0, 100))

print(arr)


def find_two_min(arr: list):
    f_min = arr[0]
    s_min = arr[0]

    for i in arr:
        if i < f_min:
            s_min = f_min
            f_min = i
        elif i < s_min:
            s_min = i

    return f_min, s_min

print(find_two_min(arr))

