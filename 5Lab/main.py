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
b1 = [0.5, 1.61, -8]
A_signs1 = ['<=', '<=', '>=']
x_signs1 = []
min_max1 = 'min'

# second
'''
x + y <= 0.5
x - y <= 3
10x + 0.1y >= -1
'''

A2 = [[1, 1], [1, -1], [10, 0.1]]
b2 = [0.5, 3, -8]
A_signs2 = ['<=', '<=', '>=']
x_signs2 = []
min_max2 = 'min'

# start point
x_start = np.array([0.5, -1.5])


def canon_to_general(z, N1, N2):
    x1 = z[:len(N1)]
    x2 = z[len(N1):len(N1) + len(N2)] - z[len(N1) + len(N2):len(N1) + len(N2) + len(N2)]
    x = np.concatenate((x1, x2))
    return x


def lp_min(x_k, A, b, A_signs, min_max, x_signs):
    c = np.append(td.calc_grad(x_k), 0)
    # print(c)
    M1, M2, N1, N2, min_max_new = manager(c, A, b, A_signs, min_max, x_signs)
    c_canon, A_canon, b_canon, A_signs_canon, x_signs_canon = common_to_canonical(c, A, b, M1, M2, N1, N2, A_signs)
    # printing(c_canon, A_canon, b_canon, A_signs_canon, min_max_new, x_signs_canon)
    z = sm.calc_global_minimum_point(c_canon, A_canon, b_canon)
    # print('z', z)
    x = canon_to_general(z, N1, N2)
    return x


def conditional_gradient(x_start, A, b, A_signs, min_max, x_signs, eps):
    x_k = x_start
    a_0 = 1/10
    limb = 0.95  # коэффициент дробления
    iters = 0
    while np.linalg.norm(td.calc_grad(x_k), ord=2) >= eps:
        # grad = td.calc_grad(x_k)
        # print('grad(x_k1):', grad)
        # print('||grad(x_k1)||:', np.linalg.norm(grad, ord=2))
        # simplex
        y_k = lp_min(x_k, A, b, A_signs, min_max, x_signs)
        if iters == 13:
            print('y_k:', y_k)
            print('grad:', td.calc_grad(x_k))
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
    # for i in range(7):
    #     conditional_gradient(x_start, A2, b2, A_signs2, min_max2, x_signs2, 10**(-i-1))
    conditional_gradient(x_start, A2, b2, A_signs2, min_max2, x_signs2, 10 ** (-4))

