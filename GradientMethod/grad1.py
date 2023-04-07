import task_data as td
import numpy as np


def calc_min(x_start, grad_eps):
    x = x_start
    points = [x]
    grad = td.calc_grad(x)
    print('x(начальная точка):', x_start)
    while (np.linalg.norm(grad, ord=2)) >= grad_eps:
        alpha = grm.calc_alpha_grm(x, alpha_eps=0.0001)
        x = x - alpha * grad
        grad = td.calc_grad(x)
        points.append(x)
        print('x(новое приближение):', x)
    return (x, points)
