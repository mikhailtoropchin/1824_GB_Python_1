"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

"""
from random import randint
with open('dz_5.txt', 'w+', encoding='utf-8') as f:
    some_number = randint(1, 50)
    while some_number > 0:
        f.write(f"{randint(1, 100)} ")
        some_number -= 1
    f.seek(0)
    numbers = f.read().split()
    result = 0
    for n in numbers:
        result += int(n)
    print(f"Сумма чисел в файле : {result}")
