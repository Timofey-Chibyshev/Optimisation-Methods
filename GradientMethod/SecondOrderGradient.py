import task_data as td
import numpy as np
import UniformMethod as uni


def calc_min(x_start, alpha_start, eps, grad_eps):
    x = x_start
    points = [x]
    grad = td.calc_grad(x)
    alpha = alpha_start
    iter_iternal = 0
    # print('alpha(начальный шаг):', alpha)
    # print('x(начальная точка):', x_start)
    while (np.linalg.norm(grad, ord=2)) >= grad_eps:
        hessian = td.calc_hessian(x)
        inv_hessian = np.linalg.inv(hessian)
        d = -np.dot(inv_hessian, grad)
        # print('d(направление):', d)
        alpha = uni.calc_gmp_uniform(0, 1, 5, eps, lambda a: td.calc_func([x[0] + a * d[0], x[1] + a * d[1]]))[0]
        # print('alpha(шаг):', alpha)
        x = x + alpha * d
        grad = td.calc_grad(x)
        points.append(x)
        # print('x(новое приближение):', x)
    return x, points
