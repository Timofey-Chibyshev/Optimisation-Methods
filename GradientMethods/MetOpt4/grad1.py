import task_data as td
import grm
import numpy as np


def calc_min(x_start, grad_eps):
    x = x_start
    points = [x]
    grad = td.calc_grad(x)
    while (np.linalg.norm(grad, ord=2)) >= grad_eps:
        alpha = grm.calc_alpha_grm(x, alpha_eps=0.01)
        x = x - alpha * grad
        grad = td.calc_grad(x)
        points.append(x)
    return (x, points)
