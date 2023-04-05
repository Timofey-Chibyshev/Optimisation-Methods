import numpy as np
import grad1
import grad2
import draw as dr
import task_data as td
import quadratic_form as qf

x_from, x_to = -2.0, 2.0
y_from, y_to = -2.0, 2.0
x_draw_func = np.linspace(x_from, x_to, 300)
y_draw_func = np.linspace(y_from, y_to, 300)
dr.add_task_func_to_ax(dr.ax,
                       x=x_draw_func,
                       y=y_draw_func)


# left_initial_points_number = 50
# # LEFT PART
# a = 0
# m = -1
# x_left_initial = np.linspace(x_from, x_to, left_initial_points_number)
# y_left_initial = -8.0 / 3.0 * x_left_initial + 1.0 / 3.0 * np.arccos(a) + 2.0 * np.pi * m / 3.0
# x_left = []
# y_left = []
# z_left = []
# left_points_number = 0
# for ind in range(left_initial_points_number):
#     if y_from <= y_left_initial[ind] <= y_to:
#         x_left.append(x_left_initial[ind])
#         y_left.append(y_left_initial[ind])
#         z_left.append(td.calc_func([x_left_initial[ind], y_left_initial[ind]]))
#         left_points_number += 1
# dr.add_points_to_ax(dr.ax, x_left, y_left, z_left, color='g')
#
#
# right_initial_points_number = 50
# # LEFT RIGHT
# a = 0
# m = 0
# x_right_initial = np.linspace(x_from, x_to, right_initial_points_number)
# y_right_initial = -8.0 / 3.0 * x_right_initial - 1.0 / 3.0 * np.arccos(a) + 2.0 * np.pi * m / 3.0
# x_right = []
# y_right = []
# z_right = []
# right_points_number = 0
# for ind in range(right_initial_points_number):
#     if y_from <= y_right_initial[ind] <= y_to:
#         x_right.append(x_right_initial[ind])
#         y_right.append(y_right_initial[ind])
#         z_right.append(td.calc_func([x_right_initial[ind], y_right_initial[ind]]))
#         right_points_number += 1
# dr.add_points_to_ax(dr.ax, x_right, y_right, z_right, color='g')


x_start_grad_1 = np.array([-0.25, -0.5])
(x_min_grad_1, points_grad_1) = grad1.calc_min(x_start=x_start_grad_1, grad_eps=0.01)

x = np.zeros(len(points_grad_1))
y = np.zeros(len(points_grad_1))
z = np.zeros(len(points_grad_1))
for ind in range(len(points_grad_1)):
    x[ind] = points_grad_1[ind][0]
    y[ind] = points_grad_1[ind][1]
    z[ind] = td.calc_func(points_grad_1[ind])
for ind in range(1, len(points_grad_1)):
    if z[ind - 1] < z[ind]:
        print("false")
dr.add_points_to_ax(dr.ax, x, y, z, 'k', text=True, text_color='k', max_ind=2)
print("Last point: ", points_grad_1[-1])
print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_1[-1]), ord=2))
print("Points number: ", len(points_grad_1))


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
dr.add_points_to_ax(dr.ax, x, y, z, 'r', text=True, text_color='r', max_ind=2)
print("Last point: ", points_grad_2[-1])
print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_2[-1]), ord=2))
print("Points number: ", len(points_grad_2))


dr.draw()
