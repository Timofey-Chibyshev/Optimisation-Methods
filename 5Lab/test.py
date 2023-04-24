from ConverterLP import *
import SimplexMethod as sm
import numpy as np
import task_data as td
from scipy.optimize import linprog as Svoy_Mega_Super_CHESTNO_SVOY_SIMPLEX

# linear constraints
# first
'''
x + y <= 0.5
x - y <= 1.61
4.84x + y >= -8
'''

A1 = [[1, 1], [1, -1], [4.84, 1]]
b1 = [0.5, 1.61, -10]
A_signs1 = ['<=', '<=', '>=']
x_signs1 = []
min_max1 = 'min'

# second
'''
x + y <= 0.5
x - y <= 3
10x + 0.1y >= -8
'''

A2 = [[1, 1], [1, -1], [10, 0.1]]
b2 = [0.5, 3, -8]
A_signs2 = ['<=', '<=', '>=']
x_signs2 = []
min_max2 = 'min'
# A2 = [[-7, 1], [1, -4], [-14, -8]]
# b2 = [3, 20, 5]
# A_signs2 = ['<=', '<=', '>=']
# x_signs2 = []
# min_max2 = 'min'

# start point for internal point
x_start_int = np.array([0.5, -1.5])
# start point for boundary point
x_start_bnd = np.array([0.5, -1.15])


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
        x0_bounds = (None, None)
        x1_bounds = (None, None)
        res = Svoy_Mega_Super_CHESTNO_SVOY_SIMPLEX(td.calc_grad(x_k), A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
        y_k = res.x
        # print('y_k:', y_k)
        # print('grad:', td.calc_grad(x_k))
        # if (iters == 14) and (eps == 10**(-4)):
        #     print('y_k:', y_k)
        #     print('grad:', td.calc_grad(x_k))
        #     test = Svoy_Mega_Super_CHESTNO_SVOY_SIMPLEX(td.calc_grad(x_k), A_ub=A11, b_ub=b11, bounds=[x0_bounds, x1_bounds])
        #     print(test.x)
        #     print(np.dot(y_k, td.calc_grad(x_k)))
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
    A_int = np.array([[1, 1], [1, -1], [-10, -0.1]])
    b_int = np.array([0.5, 3, 8])
    A_bnd = np.array([[1, 1], [1, -1], [-10, -0.1]])
    b_bnd = np.array([0.5, 1.61, 8])
    print(10*'=', "INTERNAL POINT", 10*'=')
    for i in range(7):
        conditional_gradient(x_start_int, A_int, b_int, A_signs2, min_max2, x_signs2, 10**(-i-1))
    print(20 * '=')
    print(10 * '=', "INTERNAL POINT", 10 * '=')
    for i in range(7):
        conditional_gradient(x_start_bnd, A_bnd, b_bnd, A_signs2, min_max2, x_signs2, 10 ** (-i - 1))
    # conditional_gradient(x_start, A2, b2, A_signs2, min_max2, x_signs2, 10 ** (-4))
    print(20 * '=')
