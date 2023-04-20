import matplotlib.pyplot as plt
import numpy as np
import task_data as td
import time

fig1 = plt.figure()
ax1 = fig1.add_subplot(projection='3d')
ax1.set_title('$f(x_1, x_2) = {x_1}^2 + {x_2}^2 + \cos(x_1 + 3x_2) - x_1 + 2x_2$'
              '\nМетод первого порядка с постоянным шагом')
ax1.set_xlabel('$Ox_1$')
ax1.set_ylabel('$Ox_2$')
ax1.set_zlabel('$Ox_3$')

fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
ax2.set_title('$f(x_1, x_2) = {x_1}^2 + {x_2}^2 + \cos(x_1 + 3x_2) - x_1 + 2x_2$'
              '\nМетод первого порядка с оптимальным шагом')
ax2.set_xlabel('$Ox_1$')
ax2.set_ylabel('$Ox_2$')
ax2.set_zlabel('$Ox_3$')

fig3 = plt.figure()
ax3 = fig3.add_subplot(projection='3d')
ax3.set_title('$f(x_1, x_2) = {x_1}^2 + {x_2}^2 + \cos(x_1 + 3x_2) - x_1 + 2x_2$'
              '\nМетод второго порядка')
ax3.set_xlabel('$Ox_1$')
ax3.set_ylabel('$Ox_2$')
ax3.set_zlabel('$Ox_3$')


def add_task_func_to_ax(ax, x, y):
    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = np.zeros((len(y), len(x)))
    for y_ind in range(len(y)):
        for x_ind in range(len(x)):
            arg = np.array([x[x_ind], y[y_ind]])
            z_grid[y_ind][x_ind] = td.calc_func(arg)
    ax.plot_wireframe(x_grid, y_grid, z_grid, alpha=0.3, cmap='Blues')


def add_points_to_ax(ax, x, y, z, fig, text=False, max_ind=0):
    for ind in range(0, len(x) - 1):
        point = ax.scatter(x[0], y[0], z[0], c='r', marker='*')  # начальная точка
        if text is True:
            for text_ind in range(min(len(x), max_ind)):
                ax.text(x[text_ind], y[text_ind], z[text_ind] + 0.5, str(text_ind + 1), color="black")
        # point.set_offsets([[x[ind], y[ind], z[ind]]])  # отображение нового положения точки
        ax.scatter(x[ind + 1], y[ind + 1], z[ind + 1], color='blue', marker='*')
        # # перерисовка графика и задержка на 20 мс
        # fig.canvas.draw()
        # fig.canvas.flush_events()
        # time.sleep(0.02)
        ax.plot(x, y, z, '--', c="y", linewidth=1)
    ax.scatter(x[len(x) - 1], y[len(x) - 1], z[len(x) - 1], color='green', marker='*')


def level_lines(ax, x, y, z, x_draw_func, y_draw_func, fig, Text=True):
    x1, y1 = np.meshgrid(x_draw_func, y_draw_func)  # создадим координатную плоскость из осей w1 и w2
    C = td.calc_func([x1, y1])  # пропишем функцию цели
    plt.contourf(x1, y1, C, cmap='Blues')  # построим изолинии (линии уровня)
    for ind in range(0, len(x) - 1):
        point = ax.scatter(x[0], y[0], c='red', marker='*')  # начальная точка
        if Text == True:
            for text_ind in range(min(len(x), len(x))):
                ax.text(x[text_ind], y[text_ind] + 0.1, str(text_ind + 1), color='black')
        ax.scatter(x[ind + 1], y[ind + 1], color='blue', marker='*')

        # point.set_offsets([x[ind], y[ind]])  # отображение нового положения точки
        # # перерисовка графика и задержка на 20 мс
        # fig.canvas.draw()
        # fig.canvas.flush_events()
        # time.sleep(0.02)
    ax.plot(x, y, '--', c="y", linewidth=1)
    ax.scatter(x[len(x) - 1], y[len(x) - 1], c='green', marker='*', s=50)
    ax.set_xlabel('$Ox_1$')
    ax.set_ylabel('$Ox_2$')
    plt.grid(linestyle='--')  # создадим сетку в виде прерывистой черты
