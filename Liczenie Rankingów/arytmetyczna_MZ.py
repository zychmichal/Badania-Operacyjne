"""
Parametry glownej funkcji (arytmetic_hre):
A -> Macierz
known_w-> znane wspolczynniki w. Struktura ma postac slownika (OrderedDict aby byl kompatybilny z pythonem < 3.6) gdzie klucz
to nr indeksu (liczony od 0), a wartosc to wspolczynnik
last -> boolowska wartosc true gdy znane wspolczynniki sa na koncu macierzy, false jesli jest inaczej
"""
import collections
import numpy as np
import itertools
import math
import scipy.linalg


def koczkodaj_index(mtx):
    n = np.shape(mtx)[0]
    list = []
    for x in range(n):
        list.append(x)
    all_combinations = []
    for subset in itertools.combinations(list, 3):
        all_combinations.append(subset)
    list_of_K = []
    for i,j,k in all_combinations:
        result = mtx[i][j]/(mtx[i][k]*mtx[k][j])
        K = min(abs(1 - 1/result), abs(1-result))
        list_of_K.append(K)
    return max(list_of_K)


def count_expresion(mtx, known_w):
    n = len(mtx)
    k = len(known_w)
    value = 1 - (1+math.sqrt(4*(n-1)*(n-k-2)))/(2*(n-1))
    return value



def change_rows(A, dict_of_known):
    number_known = len(dict_of_known)
    for key in dict_of_known:
        A[[key, len(A) - number_known]] = A[[len(A) - number_known, key]]
        number_known -= 1

def change_columns(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == 1:
                A[:, [j,i]] = A[:, [i,j]]


def create_matrix_when_known_element_are_not_last(A, dict_of_known):
    change_rows(A, dict_of_known)
    change_columns(A)


def create_A_and_B_matrix(A, dict_of_know):
    size_A = len(A)-len(dict_of_know)
    column_B = len(dict_of_know)
    A_new = np.zeros((size_A, size_A))
    B_new = np.zeros((size_A, column_B))
    for i in range(len(A_new)):
        for j in range(len(A_new)):
            A_new[i][j] = A[i][j]

    for i in range(len(B_new)):
        k = 0
        for j in range(len(A_new), len(A)):
            B_new[i][k] = A[i][j]
            k += 1
    return A_new, B_new


def prepare_A_new_matrix(A_new, size_A):
    for i in range(len(A_new)):
        for j in range(len(A_new)):
            if i != j:
                A_new[i][j] = (-1/(size_A-1)) * A_new[i][j]


def prepare_B_new_matrix(B_new, known_w, size_A):
    list_of_known_w = []
    for _, v in known_w.items():
        list_of_known_w.append(v)
    wektor_b = np.array([list_of_known_w]).transpose()
    B = np.matmul(B_new,wektor_b)
    B = (1/(size_A-1))* B
    return B


def fill_known_w_for_w_list(w_list, known_w):
    for k, v in known_w.items():
        w_list.insert(k, v)
    return w_list

def check_if_vector_have_only_positive_arguments(vector):
    for elem in vector:
        if elem < 0:
            return False
    return True

def arytmetic_hre(A, known_w, last):
    size_A = len(A)
    koczkodaj = koczkodaj_index(A)
    value = count_expresion(A, known_w)
    if koczkodaj > value:
        print("Koczkodaj index ({}) wiekszy od podanego wyrazenia ({}), rozwiazanie nie jest do konca godne zaufania".format(koczkodaj, value))
    else:
        print("Koczkodaj index ({}) mniejszy od podanego wyrazenia ({}), rozwiazanie jest na pewno poprawne".format(koczkodaj, value))
    if not last:
        create_matrix_when_known_element_are_not_last(A, known_w)
    A_new, B_new = create_A_and_B_matrix(A,known_w)
    prepare_A_new_matrix(A_new, size_A)
    B_new = prepare_B_new_matrix(B_new, known_w, size_A)
    x = scipy.linalg.solve(A_new,B_new)
    w_list = []
    for elem in x:
        w_list.append(float(elem))
    print("Wektor rozwiazan:")
    w_koncowe = fill_known_w_for_w_list(w_list, known_w)
    print(w_koncowe)
    if check_if_vector_have_only_positive_arguments(w_koncowe):
        print("Wszystkie wspolczynniki sa dodatnie - poprawny ranking istnieje.")
    else:
        print("Nie wszystkie wspolczynniki sa dodatnie - poprawny ranking nie istnieje.")
    print("Najlepsza opcja jest to opcja nr {}.\nJej indeks wynosi: {}".format(np.argmax(w_koncowe)+1, max(w_koncowe)))
    print('************************************************************************')


A=np.array([[1,2/3,2,5/2,5/3,5],[
3/2,1,3,10/3,3,9],[
1/2,1/3,1,4/3,7/8,5/2],[
2/5,3/10,3/4,1,5/6,12/5],[
3/5,1/3,8/7,6/5,1,3],[
1/5,1/9,2/5,5/12,1/3,1]])
known_A = collections.OrderedDict()
known_A[4] = 3
known_A[5] = 1
last_A = True

B=np.array([[1,2/5,3,7/3,1/2,1],[
5/2,1,4/7,5/8,1/3,3],[
1/3,7/4,1,1/2,2,1/2],[
3/7,8/5,2,1,4,2],[
2,3,1/2,1/4,1,1/2],[
1,1/3,2,1/2,2,1]])
known_B = collections.OrderedDict()
known_B[3] = 2
known_B[4] = 0.5
known_B[5] = 1
last_B = True


C=np.array([[1,17/4,17/20,8/5,23/6,8/3],[
4/17,1,1/5,2/5,9/10,2/3],[
20/17,5,1,21/10,51/10,10/3],[
5/8,5/2,10/21,1,5/2,11/6],[
6/23,10/9,10/51,2/5,1,19/30],[
3/8,3/2,3/10,6/11,30/19,1]])
known_C = collections.OrderedDict()
known_C[1] = 2
known_C[3] = 5
last_C = False


print('************************************************************************')
print("Macierz A:")
arytmetic_hre(A, known_A, last_A)
print("Macierz B:")
arytmetic_hre(B, known_B, last_B)
print("Macierz C:")
arytmetic_hre(C, known_C, last_C)
