import time
import matplotlib.pyplot as plt
import numpy as np
from FirstOrderGradient import first_order_gradient_optimal_step, first_order_gradient_const_step
# import grad1
import SecondOrderGradient as grad2
import draw as dr
import task_data as td

x_from, x_to = -4.0, 4.0
y_from, y_to = -4.0, 4.0
x_draw_func = np.linspace(x_from, x_to, 300)
y_draw_func = np.linspace(y_from, y_to, 300)
#
# x_min_grad1_const, points_grad1_const = first_order_gradient_const_step(eps=0.001,
#                                                                         x_start=[-0.25, -0.5])  # с постоянным шагом
# x = np.zeros(len(points_grad1_const))
# y = np.zeros(len(points_grad1_const))
# z = np.zeros(len(points_grad1_const))
# for ind in range(len(points_grad1_const)):
#     x[ind] = points_grad1_const[ind][0]
#     y[ind] = points_grad1_const[ind][1]
#     z[ind] = td.calc_func(points_grad1_const[ind])
# for ind in range(1, len(points_grad1_const)):
#     if z[ind - 1] < z[ind]:
#         print("false")
# leg = "Метод первого порядка с оптимальным шагом"
# dr.add_task_func_to_ax(dr.ax1, x=x_draw_func, y=y_draw_func)
# dr.add_points_to_ax(dr.ax1, x, y, z, dr.fig1, text=False, max_ind=len(x))
# # установим размер графика
# fig1, ax1 = plt.subplots(figsize=(5, 5))
# ax1.set_title('$f(x_1, x_2) = {x_1}^2 + {x_2}^2 + \cos(x_1 + 3x_2) - x_1 + 2x_2$'
#               '\nМетод первого порядка с постоянным шагом')
# dr.level_lines(ax1, x, y, z, x_draw_func, y_draw_func, fig1, Text=False)
#
# x_min_grad1_opt, points_grad1_opt = first_order_gradient_optimal_step(eps=0.001,
#                                                                       x_start=[-0.25, -0.5])  # с оптимальным шагом
#
# x = np.zeros(len(points_grad1_opt))
# y = np.zeros(len(points_grad1_opt))
# z = np.zeros(len(points_grad1_opt))
# for ind in range(len(points_grad1_opt)):
#     x[ind] = points_grad1_opt[ind][0]
#     y[ind] = points_grad1_opt[ind][1]
#     z[ind] = td.calc_func(points_grad1_opt[ind])
# for ind in range(1, len(points_grad1_opt)):
#     if z[ind - 1] < z[ind]:
#         print("false")
# leg = "Метод первого порядка с оптимальным шагом"
# dr.add_task_func_to_ax(dr.ax2, x=x_draw_func, y=y_draw_func)
# dr.add_points_to_ax(dr.ax2, x, y, z, dr.fig2, text=False, max_ind=len(x))
# # установим размер графика
# fig2, ax2 = plt.subplots(figsize=(5, 5))
# ax2.set_title('$f(x_1, x_2) = {x_1}^2 + {x_2}^2 + \cos(x_1 + 3x_2) - x_1 + 2x_2$'
#               '\nМетод первого порядка с оптимальным шагом')
# dr.level_lines(ax2, x, y, z, x_draw_func, y_draw_func, fig2, Text=False)
#
# x_start_grad_2 = np.array([-0.25, -0.5])
# (x_min_grad_2, points_grad_2) = grad2.calc_min(x_start=x_start_grad_2,
#                                                eps=0.001,
#                                                alpha_start=1,
#                                                grad_eps=0.01)
# x = np.zeros(len(points_grad_2))
# y = np.zeros(len(points_grad_2))
# z = np.zeros(len(points_grad_2))
# for ind in range(len(points_grad_2)):
#     x[ind] = points_grad_2[ind][0]
#     y[ind] = points_grad_2[ind][1]
#     z[ind] = td.calc_func(points_grad_2[ind])
# for ind in range(1, len(points_grad_2)):
#     if z[ind - 1] < z[ind]:
#         print("false")
#
# dr.add_task_func_to_ax(dr.ax3, x=x_draw_func, y=y_draw_func)
# dr.add_points_to_ax(dr.ax3, x, y, z, fig=dr.fig3, text=False, max_ind=len(x))
#
# # # установим размер графика
# fig3, ax3 = plt.subplots(figsize=(5, 5))
# ax3.set_title('$f(x_1, x_2) = {x_1}^2 + {x_2}^2 + \cos(x_1 + 3x_2) - x_1 + 2x_2$'
#               '\nМетод второго порядка')
# dr.level_lines(ax3, x, y, z, x_draw_func, y_draw_func, fig3, Text=False)
#
# # print("Last point: ", points_grad_2[-1])
# # print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_2[-1]), ord=2))
# # print("Points number: ", len(points_grad_2))
# # print("Решение: ", td.calc_func(points_grad_2[-1]))
# plt.show()

print("\nПостоянный шаг")
x_min_grad1_const1, points_grad1_const = first_order_gradient_const_step(eps=0.1,
                                                                         x_start=[-0.25, -0.5])  # с постоянным шагом
print("Точность",
      0.1, '\tx = {:.1f} и y = {:.1f}\t'.format(points_grad1_const[-1][0], points_grad1_const[-1][1]))
x_min_grad1_const2, points_grad1_const = first_order_gradient_const_step(eps=0.01,
                                                                         x_start=[-0.25, -0.5])  # с постоянным шагом
print("Точность",
      0.01, '\tx = {:.2f} и y = {:.2f}\t'.format(points_grad1_const[-1][0], points_grad1_const[-1][1]))

x_min_grad1_const3, points_grad1_const = first_order_gradient_const_step(eps=0.001,
                                                                         x_start=[-0.25, -0.5])  # с постоянным шагом
print("Точность",
      0.001, '\tx = {:.3f} и y = {:.3f}\t'.format(points_grad1_const[-1][0], points_grad1_const[-1][1]))

x_min_grad1_const3, points_grad1_const = first_order_gradient_const_step(eps=0.0001,
                                                                         x_start=[-0.25, -0.5])  # с постоянным шагом
print("Точность",
      0.0001, '\tx = {:.4f} и y = {:.4f}\t'.format(points_grad1_const[-1][0], points_grad1_const[-1][1]))

print("\nОптимальный шаг")
x_min_grad1_opt1, points_grad1_opt = first_order_gradient_optimal_step(eps=0.1,
                                                                       x_start=[-0.25, -0.5])  # с оптимальным шагом
print('\nx = {:.1f} y = {:.1f}\t'.format(points_grad1_opt[-1][0], points_grad1_opt[-1][1]), "Точность",
      0.1)
x_min_grad1_opt2, points_grad1_opt = first_order_gradient_optimal_step(eps=0.01,
                                                                       x_start=[-0.25, -0.5])  # с оптимальным шагом
print('\nx = {:.2f} y = {:.2f}\t'.format(points_grad1_opt[-1][0], points_grad1_opt[-1][1]), "Точность",
      0.01)
x_min_grad1_opt3, points_grad1_opt = first_order_gradient_optimal_step(eps=0.001,
                                                                       x_start=[-0.25, -0.5])  # с оптимальным шагом
print('\nx = {:.3f} y = {:.3f}\t'.format(points_grad1_opt[-1][0], points_grad1_opt[-1][1]), "Точность",
      0.001)



print("\nМетод Ньютона")
x_start_grad_2 = np.array([-0.25, -0.5])
(x_min_grad_21, points_grad_2) = grad2.calc_min(x_start=x_start_grad_2,
                                                eps=0.001,
                                                alpha_start=1,
                                                grad_eps=0.1)
print('\nx = {:.1f} y = {:.1f}\t'.format(points_grad_2[-1][0], points_grad_2[-1][1]), "Точность",
      0.1)
(x_min_grad_22, points_grad_2) = grad2.calc_min(x_start=x_start_grad_2,
                                                eps=0.001,
                                                alpha_start=1,
                                                grad_eps=0.01)
print('\nx = {:.2f} y = {:.2f}\t'.format(points_grad_2[-1][0], points_grad_2[-1][1]), "Точность",
      0.01)
(x_min_grad_23, points_grad_2) = grad2.calc_min(x_start=x_start_grad_2,
                                                eps=0.001,
                                                alpha_start=1,
                                                grad_eps=0.001)
print('\nx = {:.3f} y = {:.3f}\t'.format(points_grad_2[-1][0], points_grad_2[-1][1]), "Точность",
      0.001)
