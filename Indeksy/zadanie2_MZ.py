import numpy as np
import itertools
import math

A=np.array([[1,7,3] , [1/7,1,2] , [1/3,1/2,1]])
B=np.array([[1,1/5,7,1] , [5,1,1/2,2] , [1/7,2,1,3] , [1,1/2,1/3,1]])
C=np.array([[1,2,5,1,7] , [1/2,1,3,1/2,5] , [1/5,1/3,1,1/5,2] , [1,2,5,1,7] , [1/7,1/5,1/2,1/7,1]])

mtx_dict = {'A': A, 'B': B, 'C': C}

def find_max_real_eigenvalue(mtx):
    v, w = np.linalg.eig(mtx)
    value = 0
    for i in range(0, len(v)):
        if v[i].imag == 0:
            if v[i].real > value:
                value = v[i].real
    return value

def SattyIndex(mtx):
    lmb = find_max_real_eigenvalue(mtx)
    n = np.shape(mtx)[0]
    return (lmb - n)/(n-1)

def KoczkodajIndex(mtx):
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

def get_vector(mtx):
    n = np.shape(mtx)[0]
    vector_multiply = []
    for i in range(len(mtx[0])):
        il = 1
        for j in mtx:
            il *= j[i]
        vector_multiply.append(pow(il, 1/n))
    return vector_multiply

def GeoIndex(mtx):
    n = np.shape(mtx)[0]
    vector_of_w_i = get_vector(mtx)
    igc = 2/((n-1)*(n-2))
    suma = 0
    for i in range(n):
        for j in range(i+1, n):
            eij = mtx[i][j] * (vector_of_w_i[j]/vector_of_w_i[i])
            suma += math.log10(eij) ** 2
    return igc * suma


for k, mtx in mtx_dict.items():
    print('******************************************')
    napis = "Indeks Sattyego dla macierzy {}:".format(k)
    print(napis)
    print(SattyIndex(mtx))
    napis = "Indeks geometryczny dla macierzy {}:".format(k)
    print(napis)
    print(GeoIndex(mtx))
    napis = "Indeks Koczkodaja dla macierzy {}:".format(k)
    print(napis)
    print(KoczkodajIndex(mtx))