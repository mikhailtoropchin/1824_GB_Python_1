"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

translator = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('dz_4.txt', 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    with open('dz_4_2.txt', 'w', encoding='utf-8') as result_file:
        for l in lines:
            to_write = l.split()
            result_file.write(f"{translator[to_write[0]]} {to_write[1]} {to_write[2]}\n")

