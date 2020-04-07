from scipy.optimize import linprog

print("""
Macierz gry:

      | (1,2) | (1,3) | (2,3) | (2,4)
(1,2) |   0   |   2   |  -3   |   0
(1,3) |  -2   |   0   |   0   |   3
(2,3) |   3   |   0   |   0   |  -4
(2,4) |   0   |  -3   |   0   |   4

Do poszczegolnych wartosci dodano 4 aby wartosc gry (V) byla wieksza od 0
maxmin <= V <= minmax
""")

print("Macierz po dodaniu 4:")
A = [[4, 6, 1, 4], [2, 4, 4, 7], [7, 4, 4, 0], [4, 1, 8, 4]]
print(A)

x_bounds = (0, None)

A_1 = [[-4, -6, -1, -4], [-2, -4, -4, -7], [-7, 4, 4, 0], [-4, -1, -8, -4]]
c_1 = [1, 1, 1, 1]
b_1 = [-1, -1, -1, -1]

res_1 = linprog(c_1, A_1, b_1, bounds=(x_bounds, x_bounds, x_bounds, x_bounds))
v = 1/(res_1.fun)
result_1 = list(map(lambda result: round(result*v,5), res_1.x))

A_2 = [[4, 6, 1, 4], [2, 4, 4, 7], [7, 4, 4, 0], [4, 1, 8, 4]]
c_2 = [-1, -1, -1, -1]
b_2 = [1, 1, 1, 1]
res_2 = linprog(c_2, A_2, b_2, bounds=(x_bounds, x_bounds, x_bounds, x_bounds))
result_2 = list(map(lambda result: round(result*v,5), res_2.x))

print("Wartosc gry ze zmienionymi wartosciami: {}".format(round(v)))
print("Wartosc gry oryginalnej: {}".format(round(v)-4))
print("Strategie w rownowadze Nasha:")
print("Gracz 1: (1,2) -> {}, (1,3) -> {}, (2,3) -> {}, (2,4) -> {},".format(result_1[0], result_1[1], result_1[2], result_1[3]))
print("Gracz 2: (1,2) -> {}, (1,3) -> {}, (2,3) -> {}, (2,4) -> {},".format(result_2[0], result_2[1], result_2[2], result_2[3]))




