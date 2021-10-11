num_to_translate = input("Enter a number to translate: ")

def num_translate_adv(num):
    """Функция переводит числительные от 0 до 10 с английского на русский, но круче"""

    words = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
             "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять", "zero": "ноль"}
    if num.istitle():
        num = num.lower()
        return words.get(num).capitalize()
    return words.get(num)


print(num_translate_adv(num_to_translate))
