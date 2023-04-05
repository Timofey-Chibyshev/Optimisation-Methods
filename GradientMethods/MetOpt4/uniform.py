import math
import numpy as np


def grid_creator(a, b, n, f):
    grid_x = [a]
    grid_f = [f(a)]
    h = (b - a) / n
    for i in range(1, n + 1):
        x_i = a + i * h
        grid_x.append(x_i)
        grid_f.append(f(x_i))

    # print(*grid_x)
    # print(*grid_f)

    return grid_x, grid_f


def calc_gmp_uniform(a, b, n, eps, f):
    f_calls_number = 0
    x_0, x_1 = a, b
    iter_counter = 0
    while abs(x_1 - x_0) >= eps:
        iter_counter += 1
        grid_x, grid_f = grid_creator(x_0, x_1, n, f)
        f_calls_number += n - 1

        min_number_f, min_number_index = grid_f[1], 1

        # finding min of list
        for i in range(1, len(grid_f) - 1):
            if grid_f[i] < min_number_f:
                min_number_f, min_number_index = grid_f[i], i

        j_0, j_1 = min_number_index - 1, min_number_index + 1
        x_0, x_1 = grid_x[j_0], grid_x[j_1]
    return (x_0 + x_1)/2, f_calls_number, iter_counter


# def f(x):
#     return math.sqrt(1+x**2)+math.exp(-2*x)
#
#
# calc_gmp_uniform(0, 1, 5, 0.01, f)
