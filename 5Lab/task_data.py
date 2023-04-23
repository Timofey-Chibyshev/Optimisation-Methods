import numpy as np


# a = 1
# b = 1
# c = 3
a = 3
b = 4
c = 2


def calc_func(arg):
    x = arg[0]
    y = arg[1]
    return a*(x**2) + y**2 + np.cos(b*x + c*y) - x + 2*y


def calc_grad(arg):
    x = arg[0]
    y = arg[1]
    return np.array([2*a*x - b*np.sin(b*x + c*y) - 1, 2*y - c*np.sin(b*x + c*y) + 2])


def calc_hessian(arg):
    x = arg[0]
    y = arg[1]
    return np.array([[2*a - (b**2)*np.cos(b*x + c*y), -b*c*np.cos(b*x + c*y)],
                     [-b*c*np.cos(b*x + c*y), 2 - (c**2)*np.cos(b*x + c*y)]])
