"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы

"""

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
        result = ""
        # чтобы отобразить в нужном виде, итерируем по списку.
        for el in self.matrix:
            result += "".join(((str(el)).strip("[]").replace(",", " "), "\n"))
        return result


    def __add__(self, other):
        #создаем пустую матрицу, к-во строк и столбцов должно быть такое же, как и других матриц
        result_matrix = []
        for el in range(len(self.matrix)):
            x = [] # итерируем по количеству элементов в матрице (к-во строк)
            for i in range(len(self.matrix[0])): # чтобы найти кол-во стобцов (элементов во вложенном списке)
                x.append(0) # добавляем нули, чтобы можно было к ним прибавлять
            result_matrix.append(x) # добавляем строку с нулями, создаем матрицу по длине и ширине данной матрицы.
        for i in range(len(self.matrix)): # итерируем по строкам
            for j in range(len(self.matrix[0])): # а тут по столбцам (элементам во вложенном списке)
                result_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result_matrix) # обязательно возвращаем

# работает только при условии, что матрицы одинаковой длины и ширины, которые могут быть любыми.
mx = Matrix([[4, 2, 3], [3, 4, 2], [5, 6, 1]])
another = Matrix([[1, 2, 2], [3, 4, 4], [5, 6, 2]])
print(f"первая матрица:\n{mx}")
print(f"вторая матрица:\n{another}")
print(f"результат сложения матриц:\n{mx + another}")

