import task_data as td
import numpy as np


golden_ratio = (1 + np.sqrt(5)) / 2

# 'grm' stands for golden ratio method
def calc_grm_func(alpha, main_func_arg):
    x, y = main_func_arg[0], main_func_arg[1]
    grad = td.calc_grad(main_func_arg)
    grad_x, grad_y = grad[0], grad[1]
    a, b, c = td.a, td.b, td.c
    return a*(x**2) + y**2 - x + 2*y \
           + alpha*(-2*a*x*grad_x - 2*y*grad_y + grad_x - 2*grad_y) \
           + (alpha ** 2)*(a*(grad_x**2) + grad_y**2) \
           + np.cos(b*x + c*y - alpha*(b*grad_x + c*grad_y))


def calc_alpha_grm(main_func_arg, alpha_eps):
    alpha_from = 0.0001
    alpha_to = 0.04
    while alpha_to - alpha_from >= alpha_eps:
        alpha_1 = alpha_to - (alpha_to - alpha_from) / golden_ratio
        alpha_2 = alpha_from + (alpha_to - alpha_from) / golden_ratio
        grm_func_1, grm_func_2 = calc_grm_func(alpha_1, main_func_arg), calc_grm_func(alpha_2, main_func_arg)
        if grm_func_1 >= grm_func_2:
            alpha_from = alpha_1
        else:
            alpha_to = alpha_2
    return (alpha_from + alpha_to) / 2