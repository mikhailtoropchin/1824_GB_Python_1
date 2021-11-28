

percents = list(range(1, 101))

for percent in percents:
    if percent % 100 != 12 and percent % 100 != 13 and percent % 100 != 14 and percent % 100 != 11:  # по сути это условие можно изменить, если мы точно знаем, что будем работать только с диапазоном от 1 до 100, но в таком виде можно работать с любым.
        if percent % 10 == 1:
            print(f"{percent} процент")
        elif percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4:
            print(f"{percent} процента")
        else:
            print(f"{percent} процентов")
    else:
        print(f"{percent} процентов")

