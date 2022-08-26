"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

"""
import json


with open('dz_7.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    sum_profit = 0
    firm_count = 0
    result_list = []
    firm_profit_dict = {}
    for line in lines:
        f_line = line.split()
        firm_profit = int(f_line[-2]) - int(f_line[-1])
        if firm_profit < 0:
            firm_profit_dict.setdefault(f_line[0], firm_profit)
        else:
            firm_count += 1
            sum_profit += firm_profit
            firm_profit_dict.setdefault(f_line[0], firm_profit)
    average_dict = {"average_profit": sum_profit / firm_count}
    result_list.append(firm_profit_dict)
    result_list.append(average_dict)
    print(result_list)

with open('dz_7.json', 'w') as my_dz:
    json.dump(result_list, my_dz)

