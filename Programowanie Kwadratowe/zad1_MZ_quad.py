from cvxopt import solvers, matrix


"""
Aby obliczyc to rownanie przekształcono je do postaci:
[x1, x2][10 2] [x1]  +  [x y][-10]
        [2  1] [x2]          [-25]

jest to rownanie pomnozona przez -1 bo dla stosowanej funkcji(selvers.qp) w obliczeniach
postac kanoniczna rownania wymaga minimalizacji funkcji 
"""


Q = matrix([[10.0, 2.0], [2.0, 1.0]])
p = matrix([-10.0, -25.0])
G = matrix([[1.0, -1.0, -1.0, 0.0], [2.0, -1.0, 0.0, -1.0]])
h = matrix([10.0, -9.0, 0.0, 0.0])

solvers.options['show_progress'] = False
sol = solvers.qp(Q, p, G, h)


result = list(sol['x'])

print("Rozwiazanie: x1={}, x2={}".format(round(result[0], 2), round(result[1], 2)))
