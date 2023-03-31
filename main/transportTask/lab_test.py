import PotentialsMethod as pm
import numpy as np

prices = np.array([[ 1, 4,  7,  8,  11],
                   [ 3, 5,  9,  7,  14],
                   [ 4, 5, 12,  6, 9],
                   [ 6, 10, 11, 17, 13]], float)
a = np.array([33, 35, 17, 12], float)
b = np.array([23, 34, 5, 16, 19], float)

try:
    global_minimum_point = pm.calc_global_minimum_point(prices, a, b)
    print(global_minimum_point)
    print(np.dot(prices.flatten(), global_minimum_point))
except pm.PotentialsException as ex:
    print(ex.err_msg)