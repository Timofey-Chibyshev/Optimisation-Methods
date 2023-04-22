from ConverterLP import *
import SimplexMethod as sm
import numpy as np
import task_data as td

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
b2 = [0.5, 3, 1]
A_signs2 = ['<=', '<=', '>=']
x_signs2 = [0, 1]
min_max2 = 'min'

# start point
x_start = np.array([0.5, -1.45])


def lp_min(x_k, A, b, A_signs, min_max, x_signs):
    c = np.append(td.calc_grad(x_k), 0)
    print(c)
    M1, M2, N1, N2, min_max_new = manager(c, A, b, A_signs, min_max, x_signs)
    c_canon, A_canon, b_canon, A_signs_canon, x_signs_canon = common_to_canonical(c, A, b, M1, M2, N1, N2, A_signs)
    # printing(c_canon, A_canon, b_canon, A_signs_canon, min_max_new, x_signs_canon)
    return sm.calc_global_minimum_point(c_canon, A_canon, b_canon)[:2]


def conditional_gradient(x_start, A, b, A_signs, min_max, x_signs):
    x_k = x_start
    x_k1 = x_k
    alpha_k = 1
    limb = 0.5  # коэффициент дробления
    eps = 10 ** (-3)
    iters = 0
    while np.linalg.norm(td.calc_grad(x_k1), ord=2) >= eps:
        x_k = x_k1
        grad = td.calc_grad(x_k1)
        print('grad(x_k1):', grad)
        print('||grad(x_k1)||:', np.linalg.norm(grad, ord=2))
        iters += 1
        # simplex
        y_k = lp_min(x_k, A, b, A_signs, min_max, x_signs)
        print('y_k:', y_k)
        # direction
        s_k = y_k - x_k
        # eta
        n_k = np.dot(td.calc_grad(x_k), s_k)
        x_k1 = x_k + alpha_k * s_k
        print('x_k:', x_k)
        print('x_k1:', x_k1)
        while (td.calc_func(x_k1) - td.calc_func(x_k)) >= 0.5 * alpha_k * n_k:
            alpha_k = alpha_k * limb
            x_k = x_k1
            x_k1 = x_k + alpha_k * s_k
        print('n_k:', n_k)
        print('alpha_k:', alpha_k)
    print('min:', x_k1)
    print('dx:', (x_k1 - x_k))
    print('min_iters:', iters)


conditional_gradient(x_start, A2, b2, A_signs2, min_max2, x_signs2)

