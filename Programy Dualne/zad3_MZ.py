import numpy as np
from scipy.optimize import linprog

"""TABELA MOZLIWYCH POCIEC:

Szerokosc   |   Bele 2,1    |    Bele 4,2   |
arkusza     |               |               |
------------|---------------|---------------|
    0,5     |   4   |   1   | 8 | 5 | 2 | 0 |               
------------|-------|-------|---|---|---|---|
    1,4     |   0   |   1   | 0 | 1 | 2 | 3 |                
------------|-------|-------|---|---|---|---|
  Odpad     |  0,1  |  0,2  |0,2|0,3|0,4| 0 |               

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
A = np.array([[4, 1, 8, 5, 2, 0], [0, 1, 0, 1, 2, 3]])
b = np.array([12000, 18000])
c = np.array([0.1, 0.2, 0.2, 0.3, 0.4, 0])

#postac kanoniczna
A_c = A * (-1)
b_c = b * (-1)
c_c = c * (-1)

#rozwiazanie dla kanonicznej (dla sprawdzenia)
#res =linprog(c, A_c, b_c, bounds=(bb, bb, bb, bb, bb, bb))
#print(res.x)
#print(res.fun)

# postac dualna
A_dual = A_c.transpose()
c_dual = c_c
b_dual = b_c

#dualna postac do obliczen (postac kanoniczna lecz funkcja minimalizujaca):
A_dual_c = A_dual * (-1)
c_dual_c = c_c * (-1)
b_dual_c = b_dual

res_dual = linprog(b_dual_c, A_dual_c, c_dual_c, bounds=(bb, bb))

# Wykorzystanie rozwiazania dualnego do obcięcia rozwiązań nieoptymalnych
result_y = res_dual.x
cols_to_delete = check_if_sharp(A_dual, c_dual, result_y)
A_new, C_new = delete_unnecessary_cols(cols_to_delete, A_c, c_c)


print("Uklad rownan do obliczenia:")
print("{}x1 {}x3 = -12000".format(A_new[0][0], A_new[0][1]))
print("{}x6 = -18000\n".format(A_new[1][2]))
print("Przykladowy wynik:")

print("Metodyka cięc:\n4-> 0,5 m 0-> 1,4m (x1): 1000\n8-> 0,5 m 0-> 1,4m (x3): 1000\n0-> 0,5 m 3-> 1,4m (x6): 6000")
print("x1 i x3 to przykladowe wartosci liczba rozwiazan nieskonczona")
print("Reszta ciec nieoplacalna (zredukowana dzieki postaci dualnej)")
print("Minimalna liczba odpadów:")
print(1000*0.2 + 1000*0.1)

