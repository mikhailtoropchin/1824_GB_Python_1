"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках.

"""

from random import randint


class Solution:
    def __init__(self):
        self.n = randint(1, 10)
        self.len_arr = 2 * self.n + 1
        self.some_arr = []

        for x in range(self.len_arr):
            self.some_arr.append(randint(1, 100))


    def find_median(self, arr, half):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]

        pivot = arr[0]

        lesser = []
        greater = []
        pivots = []
        for item in arr:
            if item < pivot:
                lesser.append(item)
            elif item > pivot:
                greater.append(item)
            else:
                pivots.append(item)

        if len(lesser) > half:
            return self.find_median(lesser, half)
        elif len(lesser) + len(pivots) > half:
            return pivots[0]
        else:
            return self.find_median(greater, half - len(greater) - len(pivots))

sol = Solution()
print(sol.some_arr)
print(sol.find_median(sol.some_arr, sol.n))

