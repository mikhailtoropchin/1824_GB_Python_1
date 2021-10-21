# скрипт для записи
import sys


def main(argv):
   some_file = open("bakery.csv", "a", encoding="utf-8")
   some_file.write(f"{argv[1]}\n")
   some_file.close()


if __name__ == '__main__':
   if len(sys.argv) > 1:
      main(sys.argv)
