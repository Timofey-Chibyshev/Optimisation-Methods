import math
import numpy as np
import matplotlib.pyplot as plt


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def f(x):
    return 2*x + 1/(x**2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a, b, n = 0.2, 2.7, 100
    grid_x = [a]
    h = (b - a) / n
    for i in range(1, n + 1):
        grid_x.append(a + i*h)
    grid_fx = [f(x) for x in grid_x]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(grid_x, grid_fx, label='функция')
    ax.grid()
    ax.set_ylabel('y')  # Add an x-label to the axes.
    ax.set_xlabel('x')  # Add a y-label to the axes.
    ax.set_title("f(x)")  # Add a title to the axes.
    ax.legend()
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
