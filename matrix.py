import numpy as np
#задаём количество строк и столбцов в матрице
N = int(input("Введите количество строк (N): "))
M = int(input("Введите количество столбцов (M): "))

matrix = np.random.randint (1, 100, size=(N, M))
print("матрица:")
print(matrix)
# Транспонирование матрицы
transpose = np.transpose(matrix)
print("Транспонированая матрица:")
print(transpose)
if N==M:
    # Вычисляем определитель
    det = np.linalg.det(matrix)
    dett = np.linalg.det(transpose)
    print("Определитель матрицы:", int(round(det)))
    print("Определитель транспонированной матрицы:", int(round(dett)))
else:
    print("Матрица не квадратная, определителя нет")