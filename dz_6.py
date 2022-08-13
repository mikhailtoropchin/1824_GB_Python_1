"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""
def int_func(word):
    for l in word:
        if ord(l) in range(97, 123):
            continue
        else:
            return "Нужно вводить только английские маленькие буквы!"
    return word.capitalize()

print(int_func('text'))
