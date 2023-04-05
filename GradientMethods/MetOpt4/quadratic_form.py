import numpy as np


def quad_form(x, y):
    x_1 = x[0]
    x_2 = x[1]
    y_1 = y[0]
    y_2 = y[1]
    return (4 * y_1**2 + 2 * y_2**2 - np.cos(8 * x_1 + 3 * x_2) * (8*y_1 + 3*y_2)**2) / (y_1**2 + y_2**2)
