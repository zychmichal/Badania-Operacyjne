#Zadanie 1                   Michal Zych
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


#Zapisanie macierzy
C1 = np.array([[1, 1/7, 1/5], [7, 1, 3], [5, 1/3, 1]])
C2 = np.array([[1, 5, 9], [1/5, 1, 4], [1/9, 1/4, 1]])
C3 = np.array([[1, 4, 1/5], [1/4, 1, 1/9], [5, 9, 1]])
C4 = np.array([[1, 9, 4], [1/9, 1, 1/4], [1/4, 4, 1]])
C5 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
C6 = np.array([[1, 6, 4], [1/6, 1, 1/3], [1/4, 3, 1]])
C7 = np.array([[1, 9, 6], [1/9, 1, 1/3], [1/6, 3, 1]])
C8 = np.array([[1, 1/2, 1/2], [2, 1, 1], [2, 1, 1]])
Cpar = np.array([[1, 4, 7, 5, 8, 6, 6, 2], [1/4, 1, 5, 3, 7, 6, 6, 1/3], [1/7, 1/5, 1, 1/3, 5, 3, 3, 1/5],
                 [1/5, 1/3, 3, 1, 6, 3, 4, 1/2], [1/8, 1/7, 1/5, 1/6, 1, 1/3, 1/4, 1/7],
                 [1/6, 1/6, 1/3, 1/3, 3, 1, 1/2, 1/5], [1/6, 1/6, 1/3, 1/4, 4, 2, 1, 1/5],
                 [1/2, 3, 5, 2, 7, 5, 5, 1]])

rankingi_kategorii = [C1, C2, C3, C4, C5, C6, C7, C8]

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
print("Najlepsza opcja jest opcja nr: 2")