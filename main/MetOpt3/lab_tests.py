import fibonacci as fib
import uniform as uni
import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2 * x + 1 / (x ** 2)


a, b = 0.5, 3.5
eps = 0.1


def solution():
    pass
    # delta = 0.9 * eps
    # gmp_Dichotomy, f_calls_number_Dichotomy = dich.calc_gmp_dichotomy(a, b, delta, eps, f)
    # print("Dichotomy: gmp=", f(gmp_Dichotomy), "f calls=", f_calls_number_Dichotomy)
    #
    # t = 10
    # gmp_Fibonacci, f_calls_number_Fibonacci = fib.calc_gmp_fibonacci(a, b, t, eps, f)
    # print("Fibonacci: gmp=", f(gmp_Fibonacci), "f calls=", f_calls_number_Fibonacci)

    # n = 5
    # gmp_Uniform, f_calls_number_Uniform = uni.calc_gmp_uniform(a, b, n, eps, f)
    # print("Uniform: gmp=", f(gmp_Uniform), "f calls=", f_calls_number_Uniform)


# func
n = 5
iter_counter_main = 0
gmp_Uniform, f_calls_number_Uniform, iter_counter_main = uni.calc_gmp_uniform(a, b, n, eps, f)
print("Uniform: gmp=", f(gmp_Uniform), "f calls=", f_calls_number_Uniform, "k=", iter_counter_main)

# n per f_calls
n_tmp = [i for i in range(3, 31)]
gmp_Uniform_tmp = [list() for _ in range(6)]
f_calls_tmp = [list() for _ in range(6)]
iter = 0
iter_counter_array = [list() for _ in range(6)]
eps_array = [1, 3, 6, 9, 12, 15]
for eps_iter in eps_array:
    for n_iter in range(3, 31):
        gmp_Uniform_test, f_calls_number_Uniform_test, iter_counter_test = uni.calc_gmp_uniform(a, b, n_iter,
                                                                                                10 ** (-eps_iter), f)
        gmp_Uniform_tmp[iter].append(gmp_Uniform_test)
        f_calls_tmp[iter].append(f_calls_number_Uniform_test)
        iter_counter_array[iter].append(iter_counter_test)
    iter += 1
    # print("Uniform: gmp=", f(gmp_Uniform_test), "f calls=", f_calls_number_Uniform_test)
print(*gmp_Uniform_tmp, *f_calls_tmp, *iter_counter_array, sep='\n')

# Graphs
fig = plt.figure()

# Func
ax = fig.add_subplot(1, 1, 1)
args = np.linspace(a, b, 100)
vals = np.array([f(x) for x in args])
ax.plot(args, vals)
ax.scatter(gmp_Uniform, f(gmp_Uniform), color='m', label='gmp')
ax.grid()
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("f(x)")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()

### Graphic n per f_calls ###

fig_1, ax_1 = plt.subplots(2, 3)
args = n_tmp
iterator = 0
for i in range(2):
    for j in range(3):
        y_low = [(math.log((b - a) / (10 ** (-eps_array[iterator]))) / math.log(l/2)) * (l - 1) for l in args]
        y_up = [(math.log((b - a) / (10 ** (-eps_array[iterator]))) / math.log(l / 2)) * (l - 1)  + l - 1 for l in args]
        ax_1[i, j].plot(args, y_up, label="теоретическая оценка up")
        ax_1[i, j].plot(args, y_low, label="теоретическая оценка low")
        ax_1[i, j].plot(args, f_calls_tmp[iterator], label="фактическое количество")
        ax_1[i, j].grid()
        ax_1[i, j].set_xlabel('n')  # Add an x-label to the axes.
        ax_1[i, j].set_ylabel('f calls')  # Add a y-label to the axes.
        ax_1[i, j].set_title(f'eps = {10 ** (-eps_array[iterator])}')  # Add a title to the axes.
        ax_1[i, j].legend()
        iterator += 1
plt.show()

### Graphic f_calls per eps ###

n_eps = 5
gmp_Uniform_eps = list()
f_calls_eps = list()
iter_counter_tmp = 0
eps_ar = [10 ** (-i) for i in range(1, 16)]
for eps in range(1, 16):
    gmp_Uniform_eps_tmp, f_calls_number_Uniform_eps_tmp, iter_counter_tmp = uni.calc_gmp_uniform(a, b, n_eps, 10 ** (-eps), f)
    gmp_Uniform_eps.append(gmp_Uniform_eps_tmp)
    f_calls_eps.append(f_calls_number_Uniform_eps_tmp)
print('Вызовы по точностям:')
print(f_calls_eps, eps_ar, iter_counter_tmp, sep='\n')
f_gmp = [f(x_i) for x_i in gmp_Uniform_eps]
x_true = 1
f_true = f(x_true)
dx = [abs(x_true - x_i) for x_i in gmp_Uniform_eps]
dfx = [abs(f_true - f(x_i)) for x_i in gmp_Uniform_eps]
print('Точность:', eps_ar[:6], 'Приближенный x:', gmp_Uniform_eps[:6], 'Приближенный f(x):', f_gmp[:6],
      '|x_true - x_eps|:', dx[:6], '|f(x_true) - f(x_eps)|:', dfx[:6], 'f_calls:', f_calls_eps[:6], sep='\n')

# graph

fig_eps = plt.figure()
ax_eps = fig_eps.add_subplot(1, 1, 1)

n_ocenka = 5
args_ocenka = [((n_ocenka - 1) / math.log(n_ocenka/2)) * math.log((b - a)/i) for i in eps_ar]

args_eps = f_calls_eps
vals_eps = eps_ar

ax_eps.semilogx(vals_eps, args_eps, label='фактическая')
ax_eps.semilogx(vals_eps, args_ocenka, label='теоретическая')
ax_eps.grid()
ax_eps.set_ylabel('f calls')  # Add an x-label to the axes.
ax_eps.set_xlabel('eps')  # Add a y-label to the axes.
ax_eps.set_title("f(x)")  # Add a title to the axes.
ax_eps.legend()
plt.show()
print(f_calls_eps)
# graph ocenka 2
#
# fig_ocenka = plt.figure()
# ax_ocenka = fig_ocenka.add_subplot(1, 1, 1)
# n_ocenka = 5
# args_ocenka = [((n_ocenka - 1) / math.log(n_ocenka/2)) * math.log((b - a)/i) for i in eps_ar]
# vals_ocenka = eps_ar
# ax_ocenka.semilogx(vals_eps, args_eps)
# ax_ocenka.grid()
# ax_ocenka.set_ylabel('f calls')  # Add an x-label to the axes.
# ax_ocenka.set_xlabel('eps')  # Add a y-label to the axes.
# ax_ocenka.set_title("f(x)")  # Add a title to the axes.
# ax_ocenka.legend()
# plt.show()
