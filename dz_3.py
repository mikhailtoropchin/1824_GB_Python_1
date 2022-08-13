"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict
"""

months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
your_month = int(input("Месяц: "))
if your_month in months[:3]:
    print("Зима")
elif your_month in months[3:6]:
    print("Весна")
elif your_month in months[6:9]:
    print("Лето")
elif your_month in months[-3:]:
    print("Осень")
else:
    print("Нужно ввести значение от 1 до 12")

# Через dict
dict_months = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for key, val in dict_months.items():
    for i in val:
        if i == your_month:
            print(key)

