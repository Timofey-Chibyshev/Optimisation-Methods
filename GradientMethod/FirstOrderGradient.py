import math
from FibonacciMethod import fibonacci


def f(x):
    return x[0] * x[0] + x[1] * x[1] + math.cos(x[0] + 3 * x[1]) - x[0] + 2 * x[1]


def grad_f(x):
    return [2 * x[0] - math.sin(x[0] + 3 * x[1]) - 1, 2 * x[1] - 3 * math.sin(x[0] + 3 * x[1]) + 2]


def first_order_gradient_const_step(eps, x0):
    grad = grad_f(x0)
    x = x0
    step = 2 / (2 + 12)  # 2 / (M + m)
    points = [x[:]]
    while grad[0] ** 2 + grad[1] ** 2 > eps:
        x[0] = x[0] - step * grad[0]
        x[1] = x[1] - step * grad[1]
        grad = grad_f(x)
        points.append(x[:])
    #    print(len(points))
    return x, points


def first_order_gradient_optimal_step(eps, x0):
    grad = grad_f(x0)
    x = x0
    points = [x[:]]
    while grad[0] ** 2 + grad[1] ** 2 > eps:
        step = fibonacci(0, 1, 0.01, f, x, grad)
        x[0] = x[0] - step * grad[0]
        x[1] = x[1] - step * grad[1]
        points.append(x[:])
        grad = grad_f(x)
    # print(len(points))
    return x, points


# x, points = first_order_gradient_const_step(0.01, [-0.25, -0.5])
# #print(points)
# for k in range(len(points) - 1):
#     x_k_norm = ((x[0] - points[k][0]) ** 2 + (x[1] - points[k][1]) ** 2) ** 0.5
#     if k != 0:
#         print("q :", (x_k_norm / x_0_norm) ** (1 / k))
#         print("alpha : ", x_k_norm / x_k1_norm)
#     else:
#         x_0_norm = x_k_norm
#         x_k1_norm = x_k_norm


