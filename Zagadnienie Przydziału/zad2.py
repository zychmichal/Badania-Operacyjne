# przygotowanie macierzy
# 3x kolumny dla pierwszego 3x kolumny dla drugiego pracownika

from scipy.optimize import linear_sum_assignment
import numpy as np
matrix = np.array([[0.8, 0.8, 0.8, 0.6, 0.6, 0.6], [2, 2, 2, 1.5, 1.5, 1.5], [0.7, 0.7, 0.7, 0.6, 0.6, 0.6],
                   [0.4, 0.4, 0.4, 0.2, 0.2, 0.2], [0.2, 0.2, 0.2, 0.4, 0.4, 0.4], [0.3, 0.3, 0.3, 0.5, 0.5, 0.5]])
row, col = linear_sum_assignment(matrix)

print("Suma funkcji: ")
print(matrix[row, col].sum())
print()

print("Miejsca występowania 1 w macierzy: ")
print(row, col)
print()

print("Macierz 0 i 1:")
for j in range(len(row)):
    for i in range(len(row)):
        if i == col[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
print()

print("Odpowiedz:")
print("1 pracownik -> Z3, Z4, Z5")
print("2 pracownik -> Z1, Z2, Z6")
