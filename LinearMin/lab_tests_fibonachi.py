import fibonacci as fib
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2 * x + 1 / (x * x)


a, b = 0.5, 3.5
eps = 0.01

gmp_Fibonacci, f_calls = fib.fibonacci(a, b, eps, f)
print("Fibonacci: gmp=", gmp_Fibonacci, "f calls=", f_calls)


# Graphs
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
args = np.linspace(0.5, 3.5)
vals_fibonachi = np.array([f(x) for x in args])
ax.plot(args, vals_fibonachi)
ax.scatter(gmp_Fibonacci, f(gmp_Fibonacci), color='g')
ax.grid()
plt.show()


for i in [-1, -2, -3, -4, -5, -6]:
    eps = 10 ** i
    gmp_Fibonacci, f_calls = fib.fibonacci(a, b, eps, f)
    print(eps, f_calls)


for i in [-1, -2, -3]:
    f_call = 0
    eps = 10 ** i
    a, b = 0.5, 3.5
    while b - a > eps:
        a1, b1, f_calls1 = fib.fibonacci_with_given_n(a, b, f, n=4)
        b = b1
        a = a1
        f_call += f_calls1
    print(eps, f_call)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
args = []
vals_fibonachi = []

for i in range(1, 16):
    eps = 10 ** -i
    gmp_Fibonacci, f_calls = fib.fibonacci(a, b, eps, f)
    args.append(eps)
    vals_fibonachi.append(f_calls)

vals_uniform = [16, 28, 36, 48, 56, 68, 76, 88, 96, 108, 116, 128, 136, 148, 156]
vals_trial = [10, 16, 22, 28, 33, 40, 45, 50, 56, 60, 66, 71, 76, 81, 87]
ax.semilogx(args, vals_fibonachi, label ="Фибоначчи")
ax.semilogx(args, vals_uniform, label = "Равномерного поиска")
ax.semilogx(args, vals_trial, label = "Пробных точек")
ax.set_ylabel('f calls') # Add an x-label to the axes.
ax.set_xlabel('eps') # Add a y-label to the axes.
ax.set_title("Зависимость количества вызовов функции от точности") # Add a title to the axes.
ax.legend()
ax.grid()
plt.show()






