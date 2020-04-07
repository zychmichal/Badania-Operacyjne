import numpy as np

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



def get_vector(mtx):
    n = np.shape(mtx)[0]
    vector_multiply = []
    for i in range(len(mtx[0])):
        il = 1
        for j in mtx:
            il *= j[i]
        vector_multiply.append(pow(il, 1/n))
    return vector_multiply


def normalized_vector(vect):
    norm_eig = []
    suma = 0
    for x in vect:
        suma += x
    for x in vect:
        norm_eig.append(x/suma)
    return norm_eig

#Lista wektorow wlasnych dla macierzy kazdej z 8 kategorii
eigen_vectors = []


for mtx in rankingi_kategorii:
    eig_v = get_vector(mtx)
    norm_v = normalized_vector(eig_v)
    eigen_vectors.append(norm_v)



#Utworzenie unormowanego wektora wlasnego dla macierzy kategorii
eig_v = get_vector(Cpar)
norm_v = normalized_vector(eig_v)


#Transpozycja macierzy dla poprawnego ich zapisania
matrix_of_eigenvectors = np.transpose(np.array(eigen_vectors))
matrix = np.transpose(np.array([norm_v]))

#Obliczenie najlepszej opcji
result = np.matmul(matrix_of_eigenvectors,matrix)

print(result)
print("Najlepsza opcja jest opcja nr: 2")
print(result[1])
print("W poprzedniej metodzie najlepsza opcja rowniez nr 2.\nJej wynik to:\n [0.36914035]")
print('W metodzie GMM wyniki były bardziej oddalone od siebie przez co widać jeszcze bardziej róźnice miedzy ofertami.')

