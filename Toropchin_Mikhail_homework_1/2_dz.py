numbers = list(range(1, 1000, 2))   # создаем обычный лист нечетных чисел от 1 до 1000

for idx in range(len(numbers)):  # изменяем лист на кубы чисел
    numbers[idx] **= 3

result = 0   # переменная для сохранения результата сложения чисел, кратных 7

for num in numbers:          # кривой цикл для создания отдельных цифр из общего числа (тут максимум 9-ти значное число, нужно как-то автоматизировать)
    first_number = num // 100000000
    second_number = (num % 100000000) // 10000000
    third_number = (num % 10000000) // 1000000
    fourth_number = (num % 1000000) // 100000
    fifth_number = (num % 100000) // 10000
    sixth_number = (num % 10000) // 1000
    seventh_number = (num % 1000) // 100
    eight_number = (num % 100) // 10
    ninth_number = num % 10
    # создаем сумму отдельных цифр числа
    sum_of_numbers = first_number + second_number + third_number + fourth_number + fifth_number + sixth_number + seventh_number + eight_number + ninth_number
    # проверяем кратность этой суммы семи
    if sum_of_numbers % 7 == 0:
        result += num

print(result)
for idx in range(len(numbers)):  # добавляем 17 к каждому элементу списка, не создавая новый
    numbers[idx] += 17
result = 0 # обновили результат, чтобы не складывал с предыдущим
for num in numbers:          # кривой цикл для создания отдельных цифр из общего числа (тут максимум 9-ти значное число, нужно как-то автоматизировать)
    first_number = num // 100000000
    second_number = (num % 100000000) // 10000000
    third_number = (num % 10000000) // 1000000
    fourth_number = (num % 1000000) // 100000
    fifth_number = (num % 100000) // 10000
    sixth_number = (num % 10000) // 1000
    seventh_number = (num % 1000) // 100
    eight_number = (num % 100) // 10
    ninth_number = num % 10
    # создаем сумму отдельных цифр числа
    sum_of_numbers = first_number + second_number + third_number + fourth_number + fifth_number + sixth_number + seventh_number + eight_number + ninth_number
    # проверяем кратность этой суммы семи
    if sum_of_numbers % 7 == 0:
        result += num
print(result)

