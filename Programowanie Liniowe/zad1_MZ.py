from scipy.optimize import linprog


A = [[-1, -1, -1], [1, 1, 1], [-1, -2, -1], [0, 2, 1]]
b = [-30, 30, -10, 20]

print("wspolczynniki funkcji maksymalizujacej -> nalezalo zamienic na funkcje minimalizujaca poprzez pomnozenie przez -1")
print("zamiana konieczna ze wzgledu na funkcje linprog ktora domyslnie przyjmuje funkcje minimalizujaca")
c = [-2, -1, -3]
print(c)
print()

#Obliczenie za pomoca linprog
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)

#linprog w zalozeniu minimalizuje!!!  wiec trzeba funkcje sprowadzic do minimializacji! (w c zamienic wspolczynnniki)
res = linprog(c, A, b,bounds=(x1_bounds, x2_bounds, x3_bounds))

print("Wartosć minimalna funkcji:")
print(res.fun)
print("Poszczególne wartosci x:")
print("x1 = {} -> wartosc po zaokragleniu: 10".format(res.x[0]))
print("x2 = {} -> wartosc po zaokragleniu: 0".format(res.x[1]))
print("x3 = {} -> wartosc po zaokragleniu: 20".format(res.x[2]))
