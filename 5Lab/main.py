from ConverterLP import *
import SimplexMethod as sm
import numpy as np
import task_data as td
from scipy.optimize import linprog as Svoy_Mega_Super_CHESTNO_SVOY_SIMPLEX

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
10x + 0.1y >= -1
'''

A2 = [[1, 1], [1, -1], [10, 0.1]]
b2 = [0.5, 3, -1]
A_signs2 = ['<=', '<=', '>=']
x_signs2 = []
min_max2 = 'min'
# A2 = [[-7, 1], [1, -4], [-14, -8]]
# b2 = [3, 20, 5]
# A_signs2 = ['<=', '<=', '>=']
# x_signs2 = []
# min_max2 = 'min'

# start point
x_start = np.array([0.5, -1])


def canon_to_general(z, N1, N2):
    x1 = z[:len(N1)]
    x2 = z[len(N1):len(N1) + len(N2) - 1] - z[len(N1) + len(N2):len(N1) + len(N2) + len(N2)]
    x = np.concatenate((x1, x2))
    return x


def lp_min(x_k, A, b, A_signs, min_max, x_signs):
    c = np.append(td.calc_grad(x_k), 0)
    print(c)
    M1, M2, N1, N2, min_max_new = manager(c, A, b, A_signs, min_max, x_signs)
    c_canon, A_canon, b_canon, A_signs_canon, x_signs_canon = common_to_canonical(c, A, b, M1, M2, N1, N2, A_signs)
    printing(c_canon, A_canon, b_canon, A_signs_canon, min_max_new, x_signs_canon)
    z = sm.calc_global_minimum_point(c_canon, A_canon, b_canon)
    print('z', z)
    x = canon_to_general(z, N1, N2)
    return x


def conditional_gradient(x_start, A, b, A_signs, min_max, x_signs, eps):
    x_k = x_start
    a_0 = 1/8
    limb = 0.95  # коэффициент дробления
    iters = 0
    while np.linalg.norm(td.calc_grad(x_k), ord=2) >= eps:
        # grad = td.calc_grad(x_k)
        # print('grad(x_k1):', grad)
        # print('||grad(x_k1)||:', np.linalg.norm(grad, ord=2))
        # simplex
        # y_k = lp_min(x_k, A, b, A_signs, min_max, x_signs)
        # print(y_k)
        A11 = np.array([[1, 1], [1, -1], [-10, -0.1]])
        b11 = np.array([0.5, 3, 8])
        x0_bounds = (None, None)
        x1_bounds = (None, None)
        res = Svoy_Mega_Super_CHESTNO_SVOY_SIMPLEX(td.calc_grad(x_k), A_ub=A11, b_ub=b11, bounds=[x0_bounds, x1_bounds])
        y_k = res.x
        # print(y_k)
        # direction
        s_k = y_k - x_k
        # eta
        n_k = np.dot(td.calc_grad(x_k), s_k)
        a_k = a_0
        while (td.calc_func(x_k + a_k * s_k) - td.calc_func(x_k)) > 0.5 * a_k * n_k:
            a_k = a_k * limb
        x_k = x_k + a_k * s_k
        iters += 1
        # print(np.linalg.norm(td.calc_grad(x_k), ord=2))
        # print('y_k:', y_k)
        # print('x_k:', x_k)
        # print('n_k:', n_k)
        # print('alpha_k:', a_k)
    print('min:', x_k)
    print('min_iters:', iters)


if __name__ == '__main__':
    for i in range(7):
        conditional_gradient(x_start, A2, b2, A_signs2, min_max2, x_signs2, 10**(-i-1))
    # conditional_gradient(x_start, A2, b2, A_signs2, min_max2, x_signs2, 10 ** (-4))

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
