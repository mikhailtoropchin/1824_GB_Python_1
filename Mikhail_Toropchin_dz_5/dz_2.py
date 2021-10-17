# task: Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield


def odd_nums(max_num):
    """возвращает генератор нечетных чисел от 1 до n (включительно)"""
    nums = (num for num in range(1, max_num + 1, 2))
    return nums


odd_to_15 = odd_nums(15)
# Проверка
print(type(odd_to_15))
while True:
    print(next(odd_to_15))
