# 2.  Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
#     Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

x = 5
y = 6

def get_bit(x: int, y: int):
    print(f"Число {x}({bin(x)}), число {y}({bin(y)}): {x} & {y} = {x & y}({bin(x & y)})")
    print(f"Число {x}({bin(x)}), число {y}({bin(y)}): {x} | {y} = {x & y}({bin(x | y)})")
    print(f"Число {x}({bin(x)}), число {y}({bin(y)}): {x} ^ {y} = {x & y}({bin(x ^ y)})")
    print(f"Число {x}({bin(x)}): {x} >> 2 = {x >> 2}({bin(x >> 2)})")
    print(f"Число {x}({bin(x)}): {x} << 2 = {x << 2}({bin(x << 2)})")

get_bit(x, y)

# Побитовые операции происходят с десятичным представлением чисел, например 5 - это 101, а 6 - это 110, и при операциях
# это числа сравниваются (И - сравниваем 101 и 110 - получаем 100), другие операции по тому же принципу.


#---------------------------------------------------------------------------------------------------------------

