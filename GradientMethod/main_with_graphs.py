import time
import matplotlib.pyplot as plt
import numpy as np
from FirstOrderGradient import first_order_gradient_optimal_step, first_order_gradient_const_step
# import grad1
import SecondOrderGradient as grad2
import draw as dr
import task_data as td


x_from, x_to = -2.0, 2.0
y_from, y_to = -2.0, 2.0
x_draw_func = np.linspace(x_from, x_to, 300)
y_draw_func = np.linspace(y_from, y_to, 300)
x_start_grad = np.array([-0.25, -0.5])

x_min_grad1_const, points_grad1_const = first_order_gradient_const_step(0.01, x_start_grad)  # с постоянным шагом
print(points_grad1_const)
x_min_grad1_opt, points_grad1_opt = first_order_gradient_optimal_step(0.01, x_start_grad)  # с оптимальным шагом
print(points_grad1_opt)
# Ванька должен свой метод сюда вставить
# x_start_grad_1 = np.array([-0.25, -0.5])
# (x_min_grad_1, points_grad_1) = grad1.calc_min(x_start=x_start_grad_1, grad_eps=0.01)
# x = np.zeros(len(points_grad_1))
# y = np.zeros(len(points_grad_1))
# z = np.zeros(len(points_grad_1))
# for ind in range(len(points_grad_1)):
#     x[ind] = points_grad_1[ind][0]
#     y[ind] = points_grad_1[ind][1]
#     z[ind] = td.calc_func(points_grad_1[ind])
# for ind in range(1, len(points_grad_1)):
#     if z[ind - 1] < z[ind]:
#         print("false")
# dr.add_points_to_ax(dr.ax, x, y, z, 'k', text=True, text_color='k', max_ind=2)
# print("Last point: ", points_grad_1[-1])
# print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_1[-1]), ord=2))
# print("Points number: ", len(points_grad_1))


x_start_grad_2 = np.array([-0.25, -0.5])
(x_min_grad_2, points_grad_2) = grad2.calc_min(x_start=x_start_grad_2,
                                               eps=0.001,
                                               alpha_start=1,
                                               grad_eps=0.01)

x = np.zeros(len(points_grad_2))
y = np.zeros(len(points_grad_2))
z = np.zeros(len(points_grad_2))
for ind in range(len(points_grad_2)):
    x[ind] = points_grad_2[ind][0]
    y[ind] = points_grad_2[ind][1]
    z[ind] = td.calc_func(points_grad_2[ind])
for ind in range(1, len(points_grad_2)):
    if z[ind - 1] < z[ind]:
        print("false")
plt.ion()
dr.add_task_func_to_ax(dr.ax, x=x_draw_func, y=y_draw_func)
dr.add_points_to_ax(dr.ax, x, y, z, text=True, max_ind=len(x))
plt.ioff()
# установим размер графика
fig, ax = plt.subplots(figsize=(5, 5))
dr.level_lines(ax, x, y, x_draw_func, y_draw_func)

print("Last point: ", points_grad_2[-1])
print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_2[-1]), ord=2))
print("Points number: ", len(points_grad_2))
print("Решение: ", td.calc_func(points_grad_2[-1]))
plt.show()
