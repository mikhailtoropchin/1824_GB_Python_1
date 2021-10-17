# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего.

import sys
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# 1 вариант через list comprehension
# start = perf_counter() # для проверки скорости выполнения
result = [src[idx] for idx in range(len(src)) if idx > 0 and src[idx] > src[idx - 1]]
print(result)
# print(f"{result}, {sys.getsizeof(result)} - размер, {perf_counter() - start} - время выполнения (list comprehension)")
# list comprehension занимает больше памяти.

# 2 вариант через генератор
# start = perf_counter() # для проверки скорости выполнения
result_gen = (src[idx] for idx in range(len(src)) if idx > 0 and src[idx] > src[idx - 1])
print(*result_gen)
# print(*result_gen, f", {sys.getsizeof(result_gen)} - размер, {perf_counter() - start} - время выполнения (генератор)")
# генератор занимает меньше памяти. Время выполнения ВСЕГДА абсолютно разное, то генератор быстрее, то lc.
