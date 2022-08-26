"""
1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.

"""

with open("text_file_dz_1.txt", "w", encoding="utf-8") as my_file:
    while True:
        line = input("Введите строку для записи: ")
        if not line:
            break
        my_file.writelines(f"{line}\n")

