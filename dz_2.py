"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.

"""

with open('dz_2.txt', 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    count = 1
    for l in lines:
        print(f"Строка № - {count}, количество слов - {len(l.split())}")
        count += 1

