# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
file_1 = open("nginx_logs.txt", "r", encoding="utf-8")
content = file_1.readlines()
result = [line.split(' ')[0] for line in content]
print(max(zip((result.count(item) for item in set(result)), set(result)))) # зипуем генератор со множеством, выводим max
file_1.close()
