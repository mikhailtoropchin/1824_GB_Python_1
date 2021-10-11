num_to_translate = input("Enter a number to translate: ")


def num_translate(num):
    """Функция переводит числительные от 0 до 10 с английского на русский"""

    words = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
             "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять", "zero": "ноль"}
    return words.get(num)


print(num_translate(num_to_translate))
