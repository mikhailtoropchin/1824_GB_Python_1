default_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result_list = []

for idx in range(len(default_list)):
    # проверяем если элемент в списке это число:
    if default_list[idx].isdigit():
        result_list.append('"')
        result_list.append(f"{int(default_list[idx]):02}") # изменяем число на формат 00
        result_list.append('"')
    # проверяем если элемент НЕ число (ради чисел со знаком)
    if not default_list[idx].isdigit():
        part_list = list(default_list[idx])  # отдельный кусок в виде листа
        # если в этом куске есть знак "+", то изменяем весь кусок на формат +00
        if "+" in part_list:
            for x in part_list:
                if x.isdigit():
                    result_list.append('"')
                    result_list.append(f"+{int(x):02}")
                    result_list.append('"')
        elif "-" in part_list:
            # если в этом куске есть знак "-", то изменяем весь кусок на формат -00
            for x in part_list:
                if x.isdigit():
                    result_list.append('"')
                    result_list.append(f"-{int(x):02}")
                    result_list.append('"')
        else:
        # а если нет знаков и это не число, то просто добавляем в результат.
            result_list.append(default_list[idx])

print(" ".join(result_list))

"""
з.ы. Я потратил больше десяти часов на задачу, но один момент так и остался не решенным: 
если изменить +5 на +55, то все сломается, понимаю, что скорее всего пошел не по тому пути.
"""
