# 9.  Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = input("Введите первое число: ")
num_2 = input("Введите второе число: ")
num_3 = input("Введите третье число: ")

def find_average(f: int, s: int, t: int) -> int:
    if f.isdigit() and s.isdigit() and t.isdigit():
        f, s, t = int(f), int(s), int(t)
        if f != s != t:
            result = t
            if f < s < t:
                result = s
            elif s < f < t:
                result = f
            return result
        else:
            return "Числы должны быть разными!"
    else:
        return "Нужно ввести ЧИСЛА!"


print(find_average(num_1, num_2, num_3))

