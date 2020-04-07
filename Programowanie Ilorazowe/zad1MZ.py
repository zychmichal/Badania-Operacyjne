import numpy as np
from scipy.optimize import linprog

"""
f(x) = 3*x1 + 4*x2
g(x) = x1 + 2*x2

ograniczenia:
2*x1 + x2 >= 600
x1 + x2 <= 350
x1+ 2x2 <= 500
x1>=0, x2>=0

przeksztalcenie na problem liniowy:
y0 = 1/(x1 + 2*x2)      (xi = yi/y0)
y1 = x1/(x1 + 2*x2)
y2 = x2/(x1 + 2*x2)

f(y) = 3*y1 + 4*y2 -> f(y) = -3y1 -4y2 => min 
-2y1-y2+600y0 <= 0
y1 + y2 - 350 y0 <= 0
y1 + 2*y2 - 500 y0 <=0
-y1 - 2*y2 <= -1
y1+ 2*y2 <= 1


"""

y_bounds = (0, None)
A = [[600, -2, -1], [-350, 1, 1], [-500, 1, 2], [0, -1, -2], [0,1,2]]
b = [0, 0, 0, -1,1]
c = [0, -3, -4]

res = linprog(c, A, b, bounds=(y_bounds, y_bounds, y_bounds))

y0 = res.x[0]
y1 = res.x[1]
y2 = res.x[2]


x1 = y1/y0
x2 = y2/y0


print("Wyrob A: " + str(round(x1, 1)))
print("Wyrob B: " + str(round(x2, 1)))

"""
Dokladne wyniki:
    A -> 319.99501572348174
    B -> 1.0012389867950076e-10
"""