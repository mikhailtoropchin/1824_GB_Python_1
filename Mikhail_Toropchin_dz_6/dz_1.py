# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)

file_1 = open("nginx_logs.txt", "r", encoding="utf-8") #открыли
content = file_1.readlines() # прочитали
parsed = ((line.split(' ')[0], line.split(' ')[5].strip('"'), line.split(' ')[6]) for line in content) #порубили
print([next(parsed) for line in content]) #список кортежей
file_1.close() # закрыли
