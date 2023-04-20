import math
from FibonacciMethod import fibonacci


def f(x):
    return x[0] * x[0] + x[1] * x[1] + math.cos(x[0] + 3 * x[1]) - x[0] + 2 * x[1]


def grad_f(x):
    return [2 * x[0] - math.sin(x[0] + 3 * x[1]) - 1, 2 * x[1] - 3 * math.sin(x[0] + 3 * x[1]) + 2]

def norm(x):
    return (x[0] ** 2 + x[1] ** 2) ** 0.5


def first_order_gradient_const_step(eps, x_start):
    grad = grad_f(x_start)
    x = x_start
    step = 2 / (2 + 12)  # 2 / (M + m)
    points = [x[:]]
    while norm(grad) > eps:
        x[0] = x[0] - step * grad[0]
        x[1] = x[1] - step * grad[1]
        grad = grad_f(x)
        points.append(x[:])
    # print(points)
    return x, points


def first_order_gradient_optimal_step(eps, x_start):
    grad = grad_f(x_start)
    x = x_start
    points = [x[:]]
    while norm(grad) > eps:
        step = fibonacci(0, 1, 0.01, f, x, grad)
        x[0] = x[0] - step * grad[0]
        x[1] = x[1] - step * grad[1]
        points.append(x[:])
        grad = grad_f(x)
    # print(len(points))
    return x, points

#
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

def norm(x):
    return (x[0] ** 2 + x[1] ** 2) ** 0.5


m = 2
M = 12
x, points = first_order_gradient_optimal_step(0.01, [-0.25, -0.5])
print("Метод наискорешего спуска")
for k in range(len(points) - 1):
    x_k_norm = ((x[0] - points[k][0]) ** 2 + (x[1] - points[k][1]) ** 2) ** 0.5
    print("||x_k-x_*|| * m : {:.2f}".format(x_k_norm * m))
    print("||grad(f(x_k))||: {:.2f}".format(norm(grad_f(points[k]))))
    print("m * (1 + m/M) * (f(x_k) - f(x_*)): {:.2f}".format( m * (1 + m/M) * (f(points[k]) - f(x))))
    print("")



x, points = first_order_gradient_const_step(0.001, [-0.25, -0.5])
print("Метод постоянного шага")
for k in range(len(points) - 1):
    x_k_norm = ((x[0] - points[k][0]) ** 2 + (x[1] - points[k][1]) ** 2) ** 0.5
    if k != 0:
        print("q: {:.3f}".format(x_k_norm / x_k1_norm), )
    x_k1_norm = x_k_norm

a = 2 / (m + M)
print("{:.3f}, {:.3f}, {:.3f}".format(abs(1 - a * M), abs(1 - a * m), (M-m) / (M + m)))
