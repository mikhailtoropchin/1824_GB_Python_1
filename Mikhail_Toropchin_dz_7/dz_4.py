# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#

import os


path = "C:/Users/михаил/PycharmProjects/1824_GB_Python_1/Mikhail_Toropchin_dz_7/my_project"

result_dict = {}
count = {100:0, 1000:0, 10000:0, 100000:0} # чтобы считать

for root, dirs, files in os.walk(path):
    for item in os.scandir(root):
        if item.stat().st_size < 100 and os.path.isfile(os.path.join(root, item)):
            count[100] += 1
        elif 100 < item.stat().st_size < 1000 and os.path.isfile(os.path.join(root, item)):
            count[1000] += 1
        elif 1000 < item.stat().st_size < 10000 and os.path.isfile(os.path.join(root, item)):
            count[10000] += 1
        elif 10000 < item.stat().st_size < 100000 and os.path.isfile(os.path.join(root, item)):
            count[100000] += 1

n = 100
while n <= 100000:
    result_dict.setdefault(n, count[n])
    n *= 10

print(result_dict)
