# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

f_point = [2, 5]
s_point = [-2, -5]

def make_graph(f_point: list, s_point: list):
    k = ((f_point[1] - s_point[1])/(f_point[0] - s_point[1]))
    b = s_point[1] - k * s_point[0]
    return f'y={k}x + {b}'

print(make_graph(f_point, s_point))

# не уверен на счет этого задания, возможно не так понял

#---------------------------------------------------------------------------------------------------------------

