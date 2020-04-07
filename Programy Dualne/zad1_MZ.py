import numpy as np
from scipy.optimize import linprog


def check_if_sharp(A_dual, c_dual, ys):
    list_of_cols_to_delete = []
    n_rows, n_cols = A_dual.shape
    for i in range(n_rows):
        sum = 0
        for j in range(n_cols):
            sum+= A_dual[i][j]*ys[j]
        if round(sum, 4) > c_dual[i]:
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


x_b = (0, None)
c = np.array([2, 5, 3, 4, 1])
A = np.array([[1, 3, 2, 3, 1], [4, 6, 5, 7, 1]])
A_dual = A.transpose()
b = np.array([6, 15])
c_dual_c = c*(-1)

#Przeksztalcenie do dualnego:
c_dual_c = [x*(-1) for x in c]
A_dual_c = A_dual*(-1)


# rozwiazanie z postaci kanonicznej i funkcji minimalizujacej (dla sprawdzenia)
#res =linprog(c_dual_c, A, b, bounds=(x_b, x_b, x_b, x_b, x_b))


res_dual = linprog(b, A_dual_c, c_dual_c, bounds=(x_b, x_b))
print("Rozwiazanie funkcji problemu dualnego")
print(res_dual.fun)
print("Wyznaczone y's:")
print(res_dual.x)

cols_to_delete = check_if_sharp(A_dual, c, res_dual.x)
A_new, C_new = delete_unnecessary_cols(cols_to_delete, A, c)


res_3 = np.linalg.solve(A_new, b)
print("Wyznaczone x's:")
print(res_3)















