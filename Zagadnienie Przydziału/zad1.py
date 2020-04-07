from scipy.optimize import linear_sum_assignment
import numpy as np
matrix = np.array([[5, 7, 8, 7], [6, 4, 7, 6], [7, 5, 6, 5], [4, 3, 5, 9]])
row, col = linear_sum_assignment(matrix)

print("Suma funkcji: ")
print(matrix[row, col].sum())

print("Miejsca występowania 1 w macierzy: ")
print(row, col)

print("Macierz 0 i 1:")
for j in range(len(row)):
    for i in range(len(row)):
        if i == col[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

print("Odpowiedz:")
print("1 warsztat -> Ford")
print("2 warsztat -> Volkswagen")
print("3 warsztat -> Fiat")
print("4 warsztat -> Toyota")
