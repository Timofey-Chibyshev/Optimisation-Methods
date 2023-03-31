import matplotlib.pyplot as plt
import numpy as np


def f(x):
    global func_calls
    func_calls += 1
    return 2 * x + 1 / (x ** 2)


def trial_points(ak, bk):
    return ak + (bk - ak) / 4, ak + (2 * (bk - ak)) / 4, ak + (3 * (bk - ak)) / 4


def method_trial_points(a, b, eps):
    ak, bk = a, b
    x1, x2, x3 = trial_points(ak, bk)
    f1, f2 = f(x1), f(x2)

    while abs(bk - ak) >= eps:
        if f1 <= f2:
            # [ak , bk] -> [ak , x2]
            ak, bk = ak, x2
            x1, x2, x3 = trial_points(ak, bk)
            f2 = f1
            f1 = f(x1)
        else:
            f3 = f(x3)
            if f2 <= f3:
                # [ak , bk] -> [x1 , x3]
                ak, bk = x1, x3
                x1, x2, x3 = trial_points(ak, bk)
                f2 = f2
                f1 = f(x1)
            else:
                # [ak , bk] -> [x2 , bk]
                ak, bk = x2, bk
                x1, x2, x3 = trial_points(ak, bk)
                f2 = f3
                f1 = f(x1)

        # print("Число вызовов функции к k-oй итерации:\t", func_calls, " x: \t", (bk + ak) / 2)
    return (bk + ak) / 2


a = 0.2
b = 2.7
N = 15
func_calls = 0
f_c = []
eps = []
t2 = []
t1 = []
for i in range(0, N, 1):
    epsilon = 10 ** (-(i + 1))
    x_ = method_trial_points(a, b, epsilon)
    f_c.append(func_calls)
    eps.append(epsilon)
    t2.append((2 * (np.log((b - a) / epsilon)) / (np.log(2)) + 1))
    t1.append((1 * (np.log((b - a) / epsilon)) / (np.log(2))))
    print("Точность:\t", "{:e}".format(eps[i]), "\t\tКоличество вызовов функции:", f_c[i])
    func_calls = 0
plt.figure()
plt.grid()
plt.plot(f_c, eps, color='blue', marker='o', markersize=5, label='Опыт')
plt.plot(t2, eps, color='black', marker='o', markersize=5, label='Оценка сверху')
plt.plot(t1, eps, color='red', marker='o', markersize=5, label='Оценка снизу')
plt.title("Зависимость числа вызовов функции от точности")
plt.xlabel("Количество вызовов функции")
plt.ylabel("Точности")
plt.yscale("log")
plt.show()
