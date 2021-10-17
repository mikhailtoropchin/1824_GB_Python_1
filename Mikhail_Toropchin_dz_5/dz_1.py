# task: Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield


def odd_nums(max_num):
    """генератор нечетных чисел от 1 до n (включительно)"""
    for num in range(1, max_num + 1, 2):
        yield num


odd_to_15 = odd_nums(15)

# Проверка:
print(type(odd_to_15))
while True:
    print(next(odd_to_15))
