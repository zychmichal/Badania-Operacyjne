from scipy.optimize import linprog

print("wspolczynniki funkcji minimalizujacej")
print("funkcja linprog domyslnie przyjmuje funkcje minimalizujaca")
# funkcja ma byc zminimalizowana
c = [8, 4]
print(c)
print()


A = [[-5, -15], [-20, -5], [15, 2]]
b = [-50, -40, 60]

#Obliczenie za pomoca linprog
x1_bounds = (0, None)
x2_bounds = (0, None)

#linprog w zalozeniu minimalizuje!!!  wiec trzeba funkcje sprowadzic do minimializacji! (w c zamienic wspolczynnniki)
res = linprog(c, A, b,bounds=(x1_bounds, x2_bounds))

print("Wartosć minimalna funkcji:")
print(res.fun)
print("Poszczególne wartosci x:")
print("Steki = {}".format(res.x[0]))
print("Ziemniaki = {}".format(res.x[1]))
