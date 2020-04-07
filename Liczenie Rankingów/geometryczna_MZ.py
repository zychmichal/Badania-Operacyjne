"""
Parametry glownej funkcji (calculate_hre):
M -> Macierz
known_u-> znane wspolczynniki u. Struktura ma postac slownika gdzie klucz
to nr indeksu (liczony od 0), a wartosc to wspolczynnik
"""
import numpy as np
import scipy.linalg
import math


def create_A_matrix(n, size):
    list_of_lists = []
    for j in range(0, size):
        list =[]
        for i in range(0,size):
            if i == j:
                list.append(n-1)
            else:
                list.append(-1)
        list_of_lists.append(list)
    A_matrix = np.array(list_of_lists)
    return A_matrix


def create_b_matrix(M, dict_of_known_u):
    b_vector = []
    to_iterate = list(range(0, len(M)))
    for k in dict_of_known_u.keys():
        if k in to_iterate:
            to_iterate.remove(k)
    for j in to_iterate:
        b = 1
        for i in range(0, len(M)):
            if i != j:
                b *= M[j][i]
                if i in dict_of_known_u:
                    b *= dict_of_known_u[i]
        b_vector.append(math.log10(b))
    b_matrix = np.array([b_vector])
    b_matrix = b_matrix.transpose()
    return b_matrix


def create_u_list(A,b):
    x = scipy.linalg.solve(A, b)
    u_list = []
    for elem in x:
        u_list.append(10 ** float(elem))
    return u_list


def fill_known_u_for_u_list(u_list, known_u):
    for k, v in known_u.items():
        u_list.insert(k, v)
    return u_list


def calculate_hre(M, known_u):
    A_matrix = create_A_matrix(len(M), len(M)-len(known_u))
    b_matrix = create_b_matrix(M, known_u)
    unknown_u = create_u_list(A_matrix, b_matrix)
    not_normalized_result = fill_known_u_for_u_list(unknown_u, known_u)
    print("Wektor rozwiazan:")
    print(not_normalized_result)
    print("Najlepsza opcja jest to opcja nr {}.\nJej indeks wynosi: {}".format(np.argmax(not_normalized_result) + 1, max(not_normalized_result)))
    print('************************************************************************')
    return not_normalized_result


A=np.array([[1,2/3,2,5/2,5/3,5],[
3/2,1,3,10/3,3,9],[
1/2,1/3,1,4/3,7/8,5/2],[
2/5,3/10,3/4,1,5/6,12/5],[
3/5,1/3,8/7,6/5,1,3],[
1/5,1/9,2/5,5/12,1/3,1]])
known_A = {4: 3, 5: 1}

B=np.array([[1,2/5,3,7/3,1/2,1],[
5/2,1,4/7,5/8,1/3,3],[
1/3,7/4,1,1/2,2,1/2],[
3/7,8/5,2,1,4,2],[
2,3,1/2,1/4,1,1/2],[
1,1/3,2,1/2,2,1]])
known_B = {3: 2, 4: 0.5, 5: 1}


C=np.array([[1,17/4,17/20,8/5,23/6,8/3],[
4/17,1,1/5,2/5,9/10,2/3],[
20/17,5,1,21/10,51/10,10/3],[
5/8,5/2,10/21,1,5/2,11/6],[
6/23,10/9,10/51,2/5,1,19/30],[
3/8,3/2,3/10,6/11,30/19,1]])
known_C = {1: 2, 3: 5}

print('************************************************************************')
print("Macierz A:")
calculate_hre(A, known_A)
print("Macierz B:")
calculate_hre(B, known_B)
print("Macierz C:")
calculate_hre(C, known_C)