prices = [13, 103, 23.5, 245, 64.2, 35, 68.3, 21, 19, 24.2, 52.1, 23, 25, 31]
rub = 100
#-----------------------------------
print(id(prices)) # проверяем id у изначального списка для дальнейшего сравнения
# А: просто выводим через запятую в нужном формате:
print(" ".join([f"{int(value // rub)} руб {int(value % rub):02} коп, " for value in prices]))
# В: сортируем по возрастанию:
print(" ".join([f"{int(value // rub)} руб {int(value % rub):02} коп, " for value in sorted(prices)]))
print(id(prices)) # проверяем что список тот же
# С Сортируем по убыванию, создаем новый список:
new_prices = [f"{int(value // rub)} руб {int(value % rub):02} коп, " for value in reversed(sorted(prices))]
# D: Выводим пять самых дорогих товаров по возрастанию:
print(" ".join([f"{int(value // rub)} руб {int(value % rub):02} коп, " for value in sorted(prices)[-5:]]))
