"""
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().

"""
some_list = list(input("Введите значения через пробел: ").split())
print(f"Первоначальный список: {some_list}")

n = 0
while True:
    some_list[n], some_list[n + 1] = some_list[n + 1], some_list[n]
    n += 2
    if len(some_list) % 2 == 0:
        if n > len(some_list) - 1:
            break
    else:
        if n > len(some_list) - 2:
            break

print(f"Измененный список: {some_list}")

