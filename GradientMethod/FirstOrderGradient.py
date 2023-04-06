import math
from FibonacciMethod import fibonacci

def f(x):
    return x[0] * x[0] + x[1] * x[1] + math.cos(x[0] + 3 * x[1]) - x[0] + 2 * x[1]


def grad_f(x):
    return [2 * x[0] - math.sin(x[0] + 3 * x[1]) - 1, 2 * x[1] - 3 * math.sin(x[0] + 3 * x[1]) + 2]


def first_order_gradient_const_step(gradient, eps, step, x0):
    grad = gradient(x0)
    x = x0
    count = 1
    while grad[0] ** 2 + grad[1] ** 2 > eps:
        x[0] = x[0] - step * grad[0]
        x[1] = x[1] - step * grad[1]
        grad = gradient(x)
        count += 1
    print(count)
    return x


eps = 0.001
step = 0.1
x0 = [-0.25, -0.5]
x = first_order_gradient_const_step(grad_f, eps, step, x0)

print(x, f(x))


def first_order_gradient_optimal_step(f, gradient, eps, x0):
    grad = gradient(x0)
    x = x0
    count = 1
    while grad[0] ** 2 + grad[1] ** 2 > eps:
        step = fibonacci(0, 1, 0.01, f, x, grad)
        x[0] = x[0] - step * grad[0]
        x[1] = x[1] - step * grad[1]
        grad = gradient(x)
        count += 1
    print(count)
    return x


x0 = [-0.25, -0.5]
x = first_order_gradient_optimal_step(f, grad_f, eps, x0)
print(x, f(x))