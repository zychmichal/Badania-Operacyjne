from scipy.optimize import linprog

print("""
Macierz gry:

      |   B1  |   B2  |   B3  |
  A1  |  -2   |   8   |   2   |
  A2  |   3   |  -1   |   0   |

""")
x_bounds = (0, None)

A_1 = [[2, -3], [-8, 1], [-2, 0]]
c_1 = [1, 1]
b_1 = [-1, -1, -1]

res_1 = linprog(c_1, A_1, b_1, bounds=(x_bounds, x_bounds))
v = 1/(res_1.fun)
result_1 = list(map(lambda result: round(result*v, 5), res_1.x))

A_2 = [[-2, 8, 2], [3, -1, 0]]
c_2 = [-1, -1, -1]
b_2 = [1, 1]
res_2 = linprog(c_2, A_2, b_2, bounds=(x_bounds, x_bounds, x_bounds))
result_2 = list(map(lambda result: round(result*v, 5), res_2.x))


print("Wartosc gry: {}".format(round(v,5)))
print("Strategie w rownowadze Nasha:")
print("Gracz 1: A1 -> {}, A2 -> {}.".format(result_1[0], result_1[1]))
print("Gracz 2: B1 -> {}, B2 -> {}, B3 -> {}.".format(result_2[0], result_2[1], result_2[2]))
