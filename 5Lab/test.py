from ConverterLP import *
import SimplexMethod as sm
import numpy as np
import task_data as td
from scipy.optimize import linprog as SIMPLEX

# linear constraints
# first
'''
ограничения, когда точка на границе
x + y <= 0.5
x - y <= 1.61
-4.84x - y <= 8
'''

A1 = np.array([[1, 1], [1, -1], [-4.84, -1]])
b1 = np.array([0.5, 1.61, 8])
A_signs1 = ['<=', '<=', '<=']
x_signs1 = []
min_max1 = 'min'

A3 = np.array([[1, 1], [1, -1], [-1, -3]])
b3 = np.array([0.5, 3, 0])

# second
'''
ограничения, когда точка внутри области
x + y <= 0.5
x - y <= 3
-10x - 0.1y <= 8
'''

A2 = np.array([[1, 1], [1, -1], [-10, -0.1]])
b2 = np.array([0.5, 3, 8])
A_signs2 = ['<=', '<=', '<=']
x_signs2 = []
min_max2 = 'min'
c2 = 5.07526

# start point
x_start_1 = np.array([0.5, -1.5])
x_start_2 = np.array([0.5, -1.5])
x_start_3 = np.array([0.5, -1.5])


def conditional_gradient(x_start, A, b, c, eps):
    R = 20
    x_k = x_start
    a_0 = 0.5
    limb = 0.5  # коэффициент дробления
    iters = 0
    while np.linalg.norm(td.calc_grad(x_k), ord=2) >= eps:
        # grad = td.calc_grad(x_k)
        # print('grad(x_k1):', grad)
        # print('||grad(x_k1)||:', np.linalg.norm(grad, ord=2))
        # simplex
        x0_bounds = (None, None)
        x1_bounds = (None, None)
        res = SIMPLEX(td.calc_grad(x_k), A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
        y_k = res.x
        # print('y_k:', y_k)
        # print('grad:', td.calc_grad(x_k))
        s_k = y_k - x_k
        n_k = np.dot(td.calc_grad(x_k), s_k)
        # print("n_k:", n_k)
        a_k = a_0
        while not ((td.calc_func(x_k + a_k * s_k) - td.calc_func(x_k)) <= 0.5 * a_k * n_k):
            a_k = a_k * limb
        k = -((0.5 * n_k) / (R * np.linalg.norm(s_k, ord=2)**2))
        print(limb * k)
        print(a_k)
        print(k)
        print("\n")
        if not(limb * k <= a_k <= k):
            print("Условие не выполнено")
        x_k = x_k + a_k * s_k
        iters += 1
    print('min: {:.8f} , {:.8f}'.format(x_k[0], x_k[1]))
    print('min_iters: ', iters)


if __name__ == '__main__':
    # print("Ограничения, когда точка на границе")
    # for i in range(3):
    #     print("Точность: ", 10 ** (-i - 1))
    #     conditional_gradient(x_start_1, A1, b1, 10 ** (-i - 1))
    #     print("-----------------------------------")
    print("Ограничения, когда точка внутри области")
    for i in range(1):
        print("Точность: ", 10 ** (-i - 1))
        conditional_gradient(x_start_2, A2, b2, c2, 10 ** (-i - 1))
        print("-----------------------------------")
