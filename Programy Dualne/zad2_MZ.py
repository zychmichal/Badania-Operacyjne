import numpy as np
from scipy.optimize import linprog


def check_if_sharp(A_dual, c_dual, ys):
    list_of_cols_to_delete = []
    n_rows, n_cols = A_dual.shape
    for i in range(n_rows):
        sum = 0
        for j in range(n_cols):
            sum += A_dual[i][j]*ys[j]
        if round(sum, 5) > c_dual[i]:
            list_of_cols_to_delete.append(i)
    return list_of_cols_to_delete


def delete_unnecessary_cols(c_t_d, A, c):
    list_of_columns = list(range(A.shape[1]))
    stay_cols = []
    for el in list_of_columns:
        if el not in c_t_d:
            stay_cols.append(el)
    A_new = A[:, stay_cols]
    c_new = []
    for i in range(c.size):
        if i in stay_cols:
            c_new.append(c[i])
    return A_new, np.array(c_new)


bounds = (0, None)

#postac kanoniczna z funkcja maksymalizujaca
A = np.array([[0.5, 0.4, 0.4, 0.2], [0.4, 0.2, 0, 0.5]])
b = np.array([2000, 2800])
c = np.array([10, 14, 8, 11])

#rozwiazanie dla kanonicznej (dla sprawdzenia)
#res =linprog(c_dual_c, A, b, bounds=(bounds, bounds, bounds, bounds))
#print(res.x)
#print(res.fun)

#przeksztalcenie macierzy do postaci dualnej
A_dual = A.transpose()

#sprowadzenie dualnej do kanonicznej z funkcja minimalizujaca (aby moc obliczyc linprog)
A_dual_c = A_dual * (-1)
c_dual_c = c * (-1)

#rozwiazanie dla dualnego:
res_dual = linprog(b, A_dual_c, c_dual_c, bounds=(bounds, bounds))
result_y = res_dual.x

cols_to_delete = check_if_sharp(A_dual, c, result_y)
A_new, C_new = delete_unnecessary_cols(cols_to_delete, A, c)

print(A_new)
print(b)
#rozwiazanie dla kanonicznej zredukowanej (z funkcja przeciwna, gdyz minimalizujaca):
res = np.linalg.solve(A_new, b)
B = round(res[0], 0)
D = round(res[1], 0)

print("Produkcja wyrobów:\nB: {}\nD: {}".format(B, D))
print("Reszta wyrobów (A, C): 0")
print("Maksymalny zysk:")
print(B*14+D*11)






