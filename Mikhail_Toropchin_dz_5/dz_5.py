# Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set() # складываем во множество все уникальные числа из списка
tmp = set()
for n in src:
    if n not in tmp:
        unique.add(n)
    else:
        unique.discard(n)
    tmp.add(n)
unique_ordered = [n for n in src if n in unique] # восстанавливаем порядок
print(unique_ordered)
