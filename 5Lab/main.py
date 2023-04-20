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
x_start = np.array([0.45, -0.5])


def conditional_gradient(x_start, A, b, A_signs, min_max, x_signs):
    x_k = x_start
    alpha_k = 1
    limb = 0.5  # коэффициент дробления
    # while 1:
    c = np.append(td.calc_grad(x_k), 0)
    # s_k
    M1, M2, N1, N2, min_max_new = manager(c, A, b, A_signs, min_max, x_signs)
    c_canon, A_canon, b_canon, A_signs_canon, x_signs_canon = common_to_canonical(c, A, b1, M1, M2, N1, N2, A_signs)
    y_k = sm.calc_global_minimum_point(c_canon, A_canon, b_canon)[:2]
    s_k = y_k - x_k
    # η
    n_k = td.calc_grad(x_k) * s_k
    print(n_k)

conditional_gradient(x_start, A1, b1, A_signs1, min_max1, x_signs1)
