import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import task_data as td
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_title('$f(x_1, x_2) = {x_1}^2 + {x_2}^2 + \cos(x_1 + 3x_2) - x_1 + x_2$')
ax.set_xlabel('$Ox_1$')
ax.set_ylabel('$Ox_2$')
ax.set_zlabel('$Ox_3$')

def func_3d(ax, x, y):
    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = np.zeros((len(y), len(x)))
    for y_ind in range(len(y)):
        for x_ind in range(len(x)):
            arg = np.array([x[x_ind], y[y_ind]])
            z_grid[y_ind][x_ind] = td.calc_func(arg)
    ax.plot_surface(x_grid, y_grid, z_grid, cmap=cm.hot, lw=0.5, rstride=8, cstride=8, alpha=0.3)
    ax.contour(x_grid, y_grid, z_grid, zdir='z', offset=-2, cmap='coolwarm')
    ax.contour(x_grid, y_grid, z_grid, zdir='x', offset=-2, cmap='coolwarm')
    ax.contour(x_grid, y_grid, z_grid, zdir='y', offset=2, cmap='coolwarm')

x_from, x_to = -2.0, 2.0
y_from, y_to = -2.0, 2.0
x_draw_func = np.linspace(x_from, x_to, 300)
y_draw_func = np.linspace(y_from, y_to, 300)
func_3d(ax, x=x_draw_func, y=y_draw_func)

plt.show()

# X, Y, Z = axes3d.get_test_data(0.05)
#
# # Plot the 3D surface
# ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8,
#                 alpha=0.3)
#
# # Plot projections of the contours for each dimension.  By choosing offsets
# # that match the appropriate axes limits, the projected contours will sit on
# # the 'walls' of the graph.
