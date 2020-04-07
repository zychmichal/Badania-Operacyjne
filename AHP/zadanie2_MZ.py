#Zadanie 2                   Michal Zych
"""Utworzenie 4 macierzy na podstawie kategorii: cena, wyzywaienie, odleglosc od konferencji, parking przy hotelu
Macierz C1 -> kategoria: cena
kryterium: 20 zl roznicy -> 1 pkt
    T       K       M       B
T   1       1/3     2       3
K   3       1       4       5
M   1/2     1/4     1       2
B   1/3     1/5     1/2     1


Macierz C2 -> kategoria: wyzywienie
kryterium: 5 zl roznicy -> 1 pkt
    T       K       M       B
T   1       1       3       2
K   1       1       3       2
M   1/3     1/3     1       1/2
B   1/2     1/2     2       1


Macierz C3 -> kategoria: odleglosc
kryterium: subiektywna ocena pieszo/autobusy
    T       K       M       B
T   1       5       1/2     1/3
K   1/5     1       1/7     1/9
M   2       7       1       1/2
B   3       9       2       1


Macierz C4 -> kategoria: parking przy hotelu
kryterium: tak ->3 pkt nie 1-> pkt ocena to podzielenie A/B
    T       K       M       B
T   1       1/3     1       1/3
K   3       1       3       1
M   1       1/3     1       1/3
B   3       1       3       1

"""
import numpy as np

#funkcja znajdujaca wektor wlasny dla najwiekszej rzeczywistej wartosci wlasnej
def find_eigenvector_for_max_real_eigenvalue(mtx):
    v, w = np.linalg.eig(mtx)
    value = 0
    index = 0
    for i in range(0, len(v)):
        if v[i].imag == 0:
            if v[i].real > value:
                value = v[i].real
                index = i

    u = w[:, index]
    eigen_vector = []
    for x in u:
        eigen_vector.append(x.real)
    return eigen_vector


#Funkcja normujaca
def normalized_vector(vect):
    norm_eig = []
    suma = 0
    for x in vect:
        suma += x
    for x in vect:
        norm_eig.append(x/suma)
    return norm_eig


C1 = np.array([[1, 1/3, 2, 3], [3, 1, 4, 5], [1/2, 1/4, 1, 2], [1/3, 1/5, 1/2, 1]])
C2 = np.array([[1, 1, 3, 2], [1, 1, 3, 2], [1/3, 1/3, 1, 1/2], [1/2, 1/2, 2, 1]])
C3 = np.array([[1, 5, 1/2, 1/3], [1/5, 1, 1/7, 1/9], [2, 7, 1, 1/2], [3, 9, 2, 1]])
C4 = np.array([[1, 1/3, 1, 1/3], [3, 1, 3, 1], [1, 1/3, 1, 1/3], [3, 1, 3, 1]])
Cpar = np.array([[1, 5, 3, 4], [1/5, 1, 4, 1], [1/3, 1/4, 1, 2], [1/4, 1, 1/2, 1]])

rankingi_kategorii = [C1, C2, C3, C4]

#Lista wektorow wlasnych dla macierzy kazdej z 8 kategorii
eigen_vectors = []

#Utworzenie listy unormowanych wektorow wlasnych dla kazdej z 8 kategorii
for mtx in rankingi_kategorii:
    eig_v = find_eigenvector_for_max_real_eigenvalue(mtx)
    norm_v = normalized_vector(eig_v)
    eigen_vectors.append(norm_v)

#Utworzenie unormowanego wektora wlasnego dla macierzy kategorii
eig_v = find_eigenvector_for_max_real_eigenvalue(Cpar)
norm_v = normalized_vector(eig_v)


#Transpozycja macierzy dla poprawnego ich zapisania
matrix_of_eigenvectors = np.transpose(np.array(eigen_vectors))
matrix = np.transpose(np.array([norm_v]))

#Obliczenie najlepszej opcji
result = np.matmul(matrix_of_eigenvectors,matrix)

print(result)
print("Najlepsza opcja jest opcja nr: 2 -> Hotel MUR")