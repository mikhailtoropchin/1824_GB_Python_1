# через CLI, где аргументы - названия файлов
# первый аргумент - юзеры, второй - хобби
# третий - конечный файл (можно любое название, туда запишется результат)
import sys


def main(argv):

    users = open(argv[1], "r", encoding="utf-8")
    hobby = open(argv[2], "r", encoding="utf-8")
    users_hobby = open(argv[3], "w", encoding="utf-8")

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


if __name__ == '__main__':
   if len(sys.argv) > 1:
      main(sys.argv)
