"""
№1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9

"""

arr = []

for i in range(2, 100):
    arr.append(i)

print(arr)


def find_numbers(arr: list):
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    res_list = []
    for i in arr:
        is_div = True
        for num in numbers:
            if i % num != 0:
                is_div = False
                break
        if is_div:
            res_list.append(i)

    return res_list

print(find_numbers(arr))


# либо если я не так понял:
# for i in range(2, 10):
#     print(f"Чисел кратных {i} - {99 // i}")

