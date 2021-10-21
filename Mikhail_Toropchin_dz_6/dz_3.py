import sys
# открываем оба файла
users = open("users.csv", "r", encoding="utf-8")
hobby = open("hobby.csv", "r", encoding="utf-8")

result = {}
# читаем целиком
users_content = users.readlines()
hobby_content = hobby.readlines()
# сравниваем длину полученных списков
sub = len(users_content) - len(hobby_content)
if sub < 0:
    sys.exit(1)
while sub > 0:
    hobby_content.append(None)
    sub -= 1
for u, h in zip(users_content, hobby_content):
    if h is None:
        result.setdefault(u.strip(), h)
    else:
        result.setdefault(u.strip(), h.strip())

# записываем в файл получившийся словарь
ushob_dict = open("ushob.txt", "w", encoding="utf-8")
ushob_dict.write(str(result))
ushob_dict.close()
users.close()
hobby.close()
