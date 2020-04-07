#Zadanie 3                   Michal Zych
"""Utworzenie 3 kategorii: cena, bezpieczenstwo pojemnosc
Macierz C_cs -> kategoria: cena, podkategoria: cena samochodu
kryterium: 10000 zl roznicy -> 1 pkt
        S1         S2         S3
S1      1          1/2.83     1.92
S2      2.83       1          4.75
S3      1/1.92     1/4.75        1

C_cs = np.array([[1, 1/2.83, 1.92], [2.83, 1, 4.75], [1/1.92, 1/4.75, 1]])
Macierz C_zp -> kategoria: cena, podkategoria: zuzycie paliwa
kryterium: 1l/100 roznicy -> 1 pkt
        S1         S2       S3
S1      1          2.3      1/3.1
S2      1/2.3      1        1/5.4
S3      3.1        5.4        1
C_zp = np.array([[1, 2.3, 1/3.1], [1/2.3, 1, 1/5.4], [3.1, 5.4, 1]])

Macierz C_bez -> kategoria: bezpieczenstwo
kryterium: 0,5 roznicy -> 1 pkt
        S1       S2       S3
S1      1        2        1/2
S2      1/2      1        1/3
S3      2        3        1
C_bez = np.array([[1, 2, 1/2], [1/2, 1, 1/3], [2, 3, 1]])

Macierz C_rb -> kategoria: pojemnosc, podkategoria: rozmiar bagaznika
kryterium: 20l roznicy -> 1 pkt
        S1       S2       S3
S1      1        9/4      3/2
S2      4/9      1        3/4
S3      2/3      4/3      1
C_rb = np.array([[1, 9/4, 3/2], [4/9, 1, 3/4], [2/3, 4/3, 1]])

Macierz C_ip -> kategoria: pojemnosc, podkategoria: ilosc pasazerow
kryterium: 1 pasazer roznicy-> 1 pkt
        S1       S2       S3
S1      1        1        2
S2      1        1        2
S3      1/2      1/2      1
C_ip = np.array([[1, 1, 2], [1, 1, 2], [1/2, 1/2, 1]])

(Macierze kategorii -> ilosc punktow subiektywna ocena)
Macierz C_cena -> macierz kategorii cena:
        Cs        Zp
Cs      1         5
Zp      1/5       1
C_cena = np.array([[1, 5], [1/5, 1]])

Macierz C_poj -> macierz kategorii pojemnosc:
        Rb      Ip
Rb      1       1/3
Ip      3        1
C_poj = np.array([[1, 1/3], [3, 1]])

Macierz C_kat -> macierz kategorii:
        C       B       P
C       1       3       5
B       1/3     1       3
P       1/5     1/3     1
C_kat = np.array([[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]])
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

#DANE:

#Cena
C_cs = np.array([[1, 1/2.83, 1.92], [2.83, 1, 4.75], [1/1.92, 1/4.75, 1]])
C_zp = np.array([[1, 2.3, 1/3.1], [1/2.3, 1, 1/5.4], [3.1, 5.4, 1]])
C_cena = np.array([[1, 5], [1/5, 1]])

#Bezpieczenstwo
C_bez = np.array([[1, 2, 1/2], [1/2, 1, 1/3], [2, 3, 1]])

#pojemnosc
C_rb = np.array([[1, 9/4, 3/2], [4/9, 1, 3/4], [2/3, 4/3, 1]])
C_ip = np.array([[1, 1, 2], [1, 1, 2], [1/2, 1/2, 1]])
C_poj = np.array([[1, 1/3], [3, 1]])

#macierz kategorii
C_kat = np.array([[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]])


#OBLICZENIA DO CENY
rankingi_podkategorii_cena = [C_cs, C_zp]

#Lista wektorow wlasnych dla macierzy kazdej z 8 kategorii
eigen_vectors = []

#Utworzenie listy unormowanych wektorow wlasnych dla kazdej z 8 kategorii
for mtx in rankingi_podkategorii_cena:
    eig_v = find_eigenvector_for_max_real_eigenvalue(mtx)
    norm_v = normalized_vector(eig_v)
    eigen_vectors.append(norm_v)

#Utworzenie unormowanego wektora wlasnego dla macierzy kategorii (C_cena)
eig_v = find_eigenvector_for_max_real_eigenvalue(C_cena)
norm_v = normalized_vector(eig_v)


#Transpozycja macierzy dla poprawnego ich zapisania
matrix_of_eigenvectors = np.transpose(np.array(eigen_vectors))
matrix = np.transpose(np.array([norm_v]))

#Obliczenie najlepszej opcji dla ceny
wektor_cena = np.matmul(matrix_of_eigenvectors,matrix)


print("Porownanie samochod wzgledem ceny:")
print(wektor_cena)


#OBLICZENIA DO BEZPIECZENSTWA
eig_v = find_eigenvector_for_max_real_eigenvalue(C_bez)
norm_v = normalized_vector(eig_v)
wektor_bezpieczenstwo = np.transpose(np.array([norm_v]))
print("Porownanie samochod wzgledem bezpieczenstwa:")
print(wektor_bezpieczenstwo)


#OBLICZENIA DO POJEMNOSCI
rankingi_podkategorii_pojemnosc = [C_rb, C_ip]

#Lista wektorow wlasnych dla macierzy kazdej z 8 kategorii
eigen_vectors = []

#Utworzenie listy unormowanych wektorow wlasnych dla kazdej z 8 kategorii
for mtx in rankingi_podkategorii_pojemnosc:
    eig_v = find_eigenvector_for_max_real_eigenvalue(mtx)
    norm_v = normalized_vector(eig_v)
    eigen_vectors.append(norm_v)

#Utworzenie unormowanego wektora wlasnego dla macierzy kategorii
eig_v = find_eigenvector_for_max_real_eigenvalue(C_poj)
norm_v = normalized_vector(eig_v)


#Transpozycja macierzy dla poprawnego ich zapisania
matrix_of_eigenvectors = np.transpose(np.array(eigen_vectors))
matrix = np.transpose(np.array([norm_v]))

#Obliczenie najlepszej opcji dla pojemnosci
wektor_pojemnosc = np.matmul(matrix_of_eigenvectors, matrix)
print("Porownanie samochod wzgledem pojemnosci:")
print(wektor_pojemnosc)



#OBLICZENIA KONCOWE:

#utworzenie macierzy z 3 wektorow dla kazdej z kategorii
wektor_zlaczenia_kategorii = np.transpose(np.array([wektor_cena, wektor_bezpieczenstwo, wektor_pojemnosc]))

eig_v = find_eigenvector_for_max_real_eigenvalue(C_kat)
norm_v = normalized_vector(eig_v)
wektor_kategorii = np.transpose(np.array([norm_v]))

wyznaczenie_najlepszej_opcji = np.matmul(wektor_zlaczenia_kategorii, wektor_kategorii)

print("Porownanie samochod po uwzglednieniu wszystkich 3 kategorii:")
print(wyznaczenie_najlepszej_opcji)
print("Najlepsza opcja jest samochod nr 2")

