
# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
letter_num = int(input("Введите номер буквы в английском алфавите: "))
def number_of_letter(n: int):
    if 0 < n < 27:
        result = n + ord('a') - 1
        return chr(result)
    else:
        return 'letters out of range'

print(number_of_letter(letter_num))
#---------------------------------------------------------------------------------------------------------------

