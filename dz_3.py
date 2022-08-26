"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
with open('dz_3.txt', 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    count_workers = 0
    count_salary = 0
    for l in lines:
        result = l.split()
        salary = float(result[1])
        count_workers += 1
        count_salary += salary
        if salary < 20000:
            print(result[0], " ", salary)
    print(f"Средняя величина дохода сотрудников: {count_salary / count_workers}")

