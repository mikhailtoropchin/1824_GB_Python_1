import sys


def read_bakery(num):
   """выводит записи с номера, равного аргументу (файл bakery.csv)"""
   opened = open("bakery.csv", "r", encoding="utf-8")
   opened.seek(0)
   _ = 0
   while _ < num - 1:
      opened.readline()
      _ += 1
   while True:
      line = opened.readline().strip()
      print(line)
      if len(line) == 0:
         break


def read_full_bakery(num, sec):
   """выводит записи, начиная с номера, равного первому аргументу, по номер, равный второму аргументу, включительно"""
   opened = open("bakery.csv", "r", encoding="utf-8")
   opened.seek(0)
   _ = 0
   while _ < num - 1:
      opened.readline()
      _ += 1
   x = 0
   while x <= (sec - num):
      line = opened.readline().strip()
      print(line)
      x += 1


def main(argv):
   if len(sys.argv) == 2:
      read_bakery(int(argv[1]))
   elif len(sys.argv) == 3:
      read_full_bakery(int(argv[1]), int(argv[2]))


if __name__ == '__main__':
   if len(sys.argv) > 1:
      main(sys.argv)
   else:
      bakery = open("bakery.csv", "r", encoding="utf-8")
      content = bakery.read()
      print(content)
      bakery.close()
