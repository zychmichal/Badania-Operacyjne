import numpy as np
from scipy.optimize import linprog

"""
f(x) = cl * xl + cs * xs
g(x) = 140 xl + 250 * xs
gdzie cl,cs to odpowiednio 150,130 * kurs dolara 

ograniczenia:
2xl + 1 xs <= 9000
xl + xs <= 5500
xl + 2,5 xs <= 10000
xl >= 100
xs >= 100

Przekształcenie na problem liniowy:

y0 = 1/ (140 xl + 250 * xs)
y1 = xl/ (140 xl + 250 * xs)
y2 = xs/ (140 xl + 250 * xs)

2y1 + 1y2 - 9000y0 <= 0
y1 + y2 - 5500y0 <= 0
y1 + 2,5y2 - 10000y0 <= 0
-y1 + 100 y0 <=0
-y2 + 100 y0 <= 0

y1 > 100/(140 * 100 + 250 * 100) 
y2 > 100/(140 * 100 + 250 * 100) 
y0 > 1/(140 * 100 + 250 * 100) 

f(y) = cl * yl + cs * y2    ->  max
"""


kurs_dolara = 3.8699

cena_lakierek = 150 * kurs_dolara
cena_sportowego = 130 * kurs_dolara
y_bounds_min = 100/(140 * 100 + 250 * 100)
y0_bounds_min = 1/(140 * 100 + 250 * 100)

#y_bounds = ((y0_bounds_min, None), (y_bounds_min, None), (y_bounds_min, None))
y_bounds = ((0, None), (0, None), (0, None))

A = [[-9000, 2, 1], [-5500, 1, 1], [-10000, 1, 2.5], [100, -1, 0], [100, 0, -1], [0, -140, -250], [0, 140, 250]]
b = [0, 0, 0, 0, 0, -1, 1]
c = [0, -cena_lakierek, -cena_sportowego]

res = linprog(c, A, b, bounds=y_bounds)


y0 = res.x[0]
y1 = res.x[1]
y2 = res.x[2]


x1 = y1/y0
x2 = y2/y0

print("Lakierki: " + str(round(x1, 1)))
print("Obuwie sportowe: " + str(round(x2, 1)))

"""
Dokladne wyniki:
    A -> 4449.999992357278
    B -> 99.99999982836049
"""


