"""
№4. Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.

"""
# Решение через рекурсию, но оно не работает на больших числах:
def proof_func_rec(n: int) -> bool:
    def helper(n: int) -> int:
        if n == 1:
            return n
        result = helper(n - 1) + n
        return result
    return helper(n) == n * (n + 1) / 2

print(proof_func_rec(3))


# Решение через цикл, работает относительно быстро
def proof_func(n: int) -> bool:
    sum = 0
    x = 1
    while x <= n:
        sum += x
        x += 1
    return sum == n * (n + 1) / 2

print(proof_func(0))

