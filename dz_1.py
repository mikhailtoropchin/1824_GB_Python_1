# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def sum_of_digits(num: int) -> str:
    if 99 < num < 1000:
        first_dig = num // 100
        second_dig = (num % 100) // 10
        third_dig = (num % 100) % 10
        return f"Сумма - {first_dig + second_dig + third_dig}\nПроизведение - {first_dig * second_dig * third_dig}"
    else:
        return "Нужно ввести трехзначное число"

num = int(input("Введите трехзначное число "))
print(sum_of_digits(num))

#---------------------------------------------------------------------------------------------------------------

