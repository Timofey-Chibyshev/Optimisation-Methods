from ConverterLP import *
import SimplexMethod as sm
import numpy as np
import task_data as td
from scipy.optimize import linprog

# linear constraints
# first
'''
x + y <= 0.5
x - y <= 3
4.84x + y >= 1
'''

A1 = [[1, 1], [1, -1], [4.84, 1]]
b1 = [0.5, 3, 1]
A_signs1 = ['<=', '<=', '>=']
x_signs1 = [0, 1]
min_max1 = 'min'

# second
'''
x + y <= 0.5
x - y <= 3
10x + 0.1y >= 1
'''

A2 = [[1, 1], [1, -1], [10, 0.1]]
b2 = [4, 3, 1]
A_signs2 = ['<=', '<=', '>=']
x_signs2 = [0, 1]
min_max2 = 'min'

# start point
x_start = np.array([0.5, -1.45])


def canon_to_general(z, N1, N2):
    x1 = z[:len(N1)]
    x2 = z[len(N1) + 1:len(N1) + len(N2)] - z[len(N1) + len(N2) + 1:len(N1) + len(N2) + len(N2)]
    x = np.concatenate((x1, x2))
    return x


def lp_min(x_k, A, b, A_signs, min_max, x_signs):
    c = np.append(td.calc_grad(x_k), 0)
    # print(c)
    M1, M2, N1, N2, min_max_new = manager(c, A, b, A_signs, min_max, x_signs)
    c_canon, A_canon, b_canon, A_signs_canon, x_signs_canon = common_to_canonical(c, A, b, M1, M2, N1, N2, A_signs)
    # printing(c_canon, A_canon, b_canon, A_signs_canon, min_max_new, x_signs_canon)
    z = sm.calc_global_minimum_point(c_canon, A_canon, b_canon)
    x = canon_to_general(z, N1, N2)
    return x


def conditional_gradient(x_start, A, b, A_signs, min_max, x_signs):
    x_k = x_start
    a_0 = 1
    limb = 0.5  # коэффициент дробления
    eps = 10 ** (-1)
    iters = 0
    while np.linalg.norm(td.calc_grad(x_k), ord=2) >= eps:
        # grad = td.calc_grad(x_k)
        # print('grad(x_k1):', grad)
        # print('||grad(x_k1)||:', np.linalg.norm(grad, ord=2))
        # simplex
        y_k = np.array(lp_min(x_k, A, b, A_signs, min_max, x_signs))
        # A11 = np.array([[1, 1], [1, -1], [-10, -0.1], [0, -1]])
        # b11 = np.array([0.5, 3, -1, 0])
        # res = linprog(-td.calc_grad(x_k), A_ub=A11, b_ub=b11, bounds=(0, None))
        # y_k = res.x

        # direction
        s_k = np.array(y_k - x_k)
        # eta
        n_k = np.dot(td.calc_grad(x_k), s_k)
        a_k = a_0
        while (td.calc_func(x_k + a_k * s_k) - td.calc_func(x_k)) >= 0.5 * a_k * n_k:
            a_k = a_k * limb
        x_k = x_k + a_k * s_k
        iters += 1
        # print('y_k:', y_k)
        # print('x_k:', x_k)
        # print('n_k:', n_k)
        # print('alpha_k:', a_k)
    print('min:', x_k)
    print('min_iters:', iters)


conditional_gradient(x_start, A2, b2, A_signs2, min_max2, x_signs2)

# x + y <= 0.5
# x - y <= 3
# 10x + 0.1y >= 1

# -x + -y => -0.5
# -x + y => -3
# 10x + 0.1y => 1

# Minimize          w = 10*y1 + 15*y2 + 25*y3
# Subject to:       y1 + y2 + y3 >= 1000
#                   y1 - 2*y2    >= 0
#                             y3 >= 340
# with              y1 >= 0, y2 >= 0

# A = np.array([[-1, -1, -1], [-1, 2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0]])
# b = np.array([-1000, 0, -340, 0, 0])
# c = np.array([10, 15, 25])
#
#
# res = linprog(x_start, A_ub=A11, b_ub=b11, bounds=(0, None))
#
# print('Optimal value:', res.fun, '\nX:', res.x)
