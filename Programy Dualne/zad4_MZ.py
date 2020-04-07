import numpy as np
from scipy.optimize import linprog

"""TABELA MOZLIWYCH POCIEC:

Dlugosc     |            drut: 30 cm            |
gwozdzia    |                                   |
------------|---|---|---|---|---|---|---|---|---|
     11     | 0 | 0 | 1 | 0 | 1 | 0 | 2 | 2 | 1 |  
------------|---|---|---|---|---|---|---|---|---|
      8     | 0 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 2 |       
------------|---|---|---|---|---|---|---|---|---|
      5     | 6 | 4 | 3 | 2 | 2 | 1 | 0 | 5 | 0 |     
------------|---|---|---|---|---|---|---|---|---|
  Odpad     | 0 | 2 | 4 | 4 | 1 | 1 | 0 | 3 | 3 |     
"""


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

#bounds
bb = (0, None)

# funkcja minimalizujaca (w postaci kanonicznej zamieniona na maksymalizujaca)
c = np.array([0, 2, 4, 4, 1, 1, 0, 3, 3])

#postac kanoniczna
A_c = np.array([[6, 4, 3, 2, 2, 1, 0, 5, 0], [-6, -4, -3, -2, -2, -1, -0, -5, 0], [0, 1, 0, 2, 1, 3, 1, 0 ,2], [-0, -1, -0, -2, -1, -3, -1, 0, -2], [0, 0, 1, 0, 1, 0, 2, 2, 1], [-0, -0, -1, -0, -1, -0, -2, -2, -1]])
b_c = np.array([27000, -27000, 24000, -24000, 12000, -12000])
c_c = c * (-1)

#rozwiazanie dla kanonicznej (dla sprawdzenia)
#res =linprog(c, A_c, b_c, bounds=(bb, bb, bb, bb, bb, bb, bb))
#print(res.x)
#print(res.fun)

# postac dualna:
A_dual = A_c.transpose()
c_dual = c_c
b_dual = b_c

#dualna postac do obliczen (postac kanoniczna lecz funkcja minimalizujaca):
A_dual_c = A_dual * (-1)
c_dual_c = c_c * (-1)
b_dual_c = b_dual

res_dual = linprog(b_dual_c, A_dual_c, c_dual_c, bounds=(bb, bb, bb, bb, bb, bb))

# Wykorzystanie rozwiazania dualnego do obcięcia rozwiązań nieoptymalnych
result_y = res_dual.x
cols_to_delete = check_if_sharp(A_dual, c_dual, result_y)
A_new, C_new = delete_unnecessary_cols(cols_to_delete, A_c, c_c)

res =linprog(C_new * (-1), A_new, b_c, bounds=(bb, bb, bb))

print("Minimalna liczba odpadów:")
print(round(res.fun, 0))
print("Metodyka cięc:\n0-> 11 cm 0-> 8cm 6-> 5cm: {}\n0-> 11 cm 3-> 8cm 1-> 5cm: {}\n2-> 11 cm 1-> 8cm 0-> 5cm: {}".format(round(res.x[0], 0), round(res.x[1], 0), round(res.x[2], 0)))
print("Reszta ciec nieoplacalna (zredukowana dzieki postaci dualnej)")


print("Istnieje tez rozwiazanie nie zakladajace rownosci w liczbie wyprodukowanych gwozdzi:")
#postac kanoniczna
A_c = np.array([[6, 4, 3, 2, 2, 1, 0, 5, 0], [0, 1, 0, 2, 1, 3, 1, 0, 2], [0, 0, 1, 0, 1, 0, 2, 2, 1]]) * (-1)
b_c = np.array([27000, 24000, 12000]) * (-1)
c_c = c * (-1)

# postac dualna:
A_dual = A_c.transpose()
c_dual = c_c
b_dual = b_c

#dualna postac do obliczen (postac kanoniczna lecz funkcja minimalizujaca):
A_dual_c = A_dual * (-1)
c_dual_c = c_c * (-1)
b_dual_c = b_dual

res_dual = linprog(b_dual_c, A_dual_c, c_dual_c, bounds=(bb, bb, bb))

# Wykorzystanie rozwiazania dualnego do obcięcia rozwiązań nieoptymalnych
result_y = res_dual.x
cols_to_delete = check_if_sharp(A_dual, c_dual, result_y)
A_new, C_new = delete_unnecessary_cols(cols_to_delete, A_c, c_c)

print("Uklad rownan do obliczenia:")
print("{}x1 >= {}".format(A_new[0][0], b_c[0]))
print("{}x7 >= {}".format(A_new[1][1], b_c[1]))
print("{}x7 >= {}\n".format(A_new[2][1], b_c[2]))
print("Nie wytworzy się żaden odpad lecz wytworzymy 48000 srub 11 cm (4x wiecej)")
