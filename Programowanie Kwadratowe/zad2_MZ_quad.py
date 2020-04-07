from cvxopt import solvers, matrix

Q = matrix([[11.4312, 1.1701, 0.1232, 1.6619, 2.0254], [1.1701, 7.7723, 0.4983, 1.1374, 1.7056],
            [0.1232, 0.4983, 5.1598, -1.3094, -0.6307], [1.6619, 1.1374, -1.3094, 20.2858, 2.2824],
            [2.0254, 1.7056, -0.6307, 2.2824, 4.3189]])
p = matrix([0.0, 0.0, 0.0, 0.0, 0.0])
G = matrix([[-0.94, -1.0, 0.0, 0.0, 0.0, 0.0], [-1.20, 0.0, -1.0, 0.0, 0.0, 0.0], [0.02, 0.0, 0.0, -1.0, 0.0, 0.0],
            [-0.81, 0.0, 0.0, 0.0, -1.0, 0.0], [-0.45, 0.0, 0.0, 0.0, 0.0, -1.0]])
h = matrix([-1, 0.0, 0.0, 0.0, 0.0, 0.0])

A = matrix([1.0, 1.0, 1.0, 1.0, 1.0], (1,5))
b = matrix([1.0])
solvers.options['show_progress'] = False
sol = solvers.qp(Q, p, G, h, A, b)


result = list(sol['x'])
print("Rozwiazanie dokladne:")
print(result)
print()

print("Rozwiazanie [%] : spolka1 = {}%, spolka2 = {}%, spolka3 = {}%, spolka4 = {}%, spolka5 = {}%.".format(round(100*result[0], 2), round(100*result[1], 2),
                                                                                           round(100*result[2], 2), round(100*result[3], 2),
                                                                                           round(100*result[4], 2)))

