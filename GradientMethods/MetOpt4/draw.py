import matplotlib.pyplot as plt
import numpy as np
import task_data as td


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_title('$f(x_1, x_2) = 2{x_1}^2 + {x_2}^2 + \cos(8x_1 + 3x_2) - x_1 + 2x_2$')
ax.set_xlabel('$Ox_1$')
ax.set_ylabel('$Ox_2$')
ax.set_zlabel('$Ox_3$')


def add_task_func_to_ax(ax, x, y):
    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = np.zeros((len(y), len(x)))
    for y_ind in range(len(y)):
        for x_ind in range(len(x)):
            arg = np.array([x[x_ind], y[y_ind]])
            z_grid[y_ind][x_ind] = td.calc_func(arg)
    ax.plot_wireframe(x_grid, y_grid, z_grid, alpha=0.3)


def add_points_to_ax(ax, x, y, z, color, text=False, text_color='r', max_ind = 0):
    for ind in range(len(x)):
        if text is True:
            for text_ind in range(min(len(x), max_ind)):
                ax.text(x[text_ind], y[text_ind], z[text_ind] + 0.5, str(text_ind + 1), color=text_color)
        ax.scatter(x[ind], y[ind], z[ind], color=color, marker='*')


def draw():
    plt.show()
