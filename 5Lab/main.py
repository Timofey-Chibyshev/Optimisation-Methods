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


c1 = td.calc_grad(x_start)

c1 = np.append(c1, 0)

M1, M2, N1, N2, min_max_new = manager(c1, A1, b1, A_signs1, min_max1, x_signs1)

c_canon, A_canon, b_canon, A_signs_canon, x_signs_canon = common_to_canonical(c1, A1, b1, M1, M2, N1, N2, A_signs1)

try:
    y_k = sm.calc_global_minimum_point(c_canon, A_canon, b_canon)
    print('\n', y_k)
except sm.SimplexException as ex:
    print(ex.err_msg)

s_k = y_k[:2] - x_start
print(s_k)
