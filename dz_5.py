"""
№5. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

"""
# Вводимые данные
numbers = input("Введите последовательность чисел без пробела: ")
n = int(input("Введите цифру, которую нужно посчитать: "))


# Вариант решения математический:
def count_number_diff(number: int, x: int) -> int:
    count = 0
    while number > 0:
        if number % 10 == x:
            count += 1
        number = number // 10
    return count

print(f'Цифра {n} встречается {count_number_diff(int(numbers), n)} раз(а)')



# Вариант решения через строку:
def count_number(numbers: str, d: int) -> str:
    count = 0
    for i in numbers:
        if int(i) == d:
            count += 1
    return count

print(f'Цифра {n} встречается {count_number(numbers, n)} раз(а)')

