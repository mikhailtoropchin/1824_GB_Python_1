# когда объём данных в файлах превышает объём ОЗУ
import sys

users = open("users.csv", "r", encoding="utf-8")
hobby = open("hobby.csv", "r", encoding="utf-8")
users_hobby = open("users_hobby.txt", "w", encoding="utf-8")

while True:
    h = hobby.readline().strip()
    u = users.readline().strip()
    if len(u) == 0 and len(h) > 0:
        sys.exit(1)
    elif len(u) == 0 and len(h) == 0:
        break
    elif len(h) > 0 and len(u) > 0:
        users_hobby.write(f"{u}: {h}\n")
    elif len(h) == 0 and len(u) > 0:
        users_hobby.write(f"{u}: {None}\n")

users_hobby.close()
users.close()
hobby.close()
