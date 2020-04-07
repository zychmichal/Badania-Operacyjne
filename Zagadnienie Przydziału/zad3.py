# 1. sprawic by w kazdym wierszu i kolumnie bylo co najmniej jedno 0
# (po kazdym wierszu i kazdej kolumnie odejmujemy w nim najmniejsza wartosc)

# 2. znalezc minimalne pokrycie kolumn i wierszy zeby kazde 0 bylo przekreslone
# (wybranie i przekreslenie jakiegos wierszu)
# (jesli mamy mniej przekreslen niz rozmiar macierzy to trzeba ja przeksztalcic)

# 3. liczba kresek < rozmiar macierzy:
# znajdujemy minimum nieprzekreslone odejmujemy od nie przekreslonych wartosci
# i dodajemy do podwojnie przekreslonych wartosci i wracam do punktu 2

# 4 te zera wskazuja potencjalne miejsca do przydzielenia zadan
# jest takie wybranie wierszy i kolumn zeby kazdy wiersz i kazda kolumna miala 1 jedynke



# max zamiast mina -> przemnozyc przez -1 wszystkie wartosci
# lub aij := max wartosc w macierzy - aij
# pracownicy =/ liczbie zadan
# liczba zadan < pracownicy
# dodajemy fikcyjne wiersze z maxami
#liczba zadan > pracownicy
# 1 pracownik z 2 zadaniami jest rownowazny 2 pracownikom z 1 zadaniem
# robienie klonow
# gdy jest zadanie ktore dany pracownik nie moze wykonac
# wpisujemy absurdalnie wielka liczbe w takim miejscu macierzy



from scipy.optimize import linear_sum_assignment
import numpy as np
matrix = np.array([[5.6, 3.2, 4.4, 4.7, 3.2], [6, 3.5, 4.6, 4.5, 3.2], [0, 4, 5, 4.8, 3.2], [0, 3.8, 4.7, 4.8, 3.2],
                   [4.8, 4, 4.5, 4.2, 3.2]])
matrix = -1 * matrix
row, col = linear_sum_assignment(matrix)

print("Miejsca występowania 1 w macierzy: ")
print(row, col)
print()

print("Macierz 0 i 1:")
for j in range(len(row)):
    for i in range(len(row)):
        if i == col[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
print()


#przetworzenie funkcji wyniku (usuniecie z niej oferty dodanej do poprawnego uzupelnienia algorytmu)
result = matrix[row, col].sum()
result += 3.2
print("Wynik dla funkcji bez stanu dołożonego")
print(result * (-1))
print()


print("Odpowiedz:")
print("PKO PB -> brak")
print("PEKAO SA -> jednodniowa")
print("Milenium -> trzymiesieczna")
print("ING -> szesciomiesieczna")
print("Mbank -> jednomiesięczna")

