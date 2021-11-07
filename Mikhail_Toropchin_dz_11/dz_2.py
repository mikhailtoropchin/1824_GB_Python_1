class MyZeroDivision(Exception):
    def __str__(self):
        return "На ноль делить нельзя!"

a = int(input("Введите ЧТО делить: "))
z = int(input("Введите НА что делить: "))
try:
    if z == 0:
        raise MyZeroDivision
    x = int(a)/z
except MyZeroDivision as mr:
    print(mr)




