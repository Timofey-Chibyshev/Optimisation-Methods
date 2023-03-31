from numpy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from ConverterLP import *
from ConverterDualTask import *
from ConverterDualTask import *
from SimplexMethod import *
import SimplexMethod as sm
import numpy as np
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from functools import partial

# #def test():
#     A_tmp = [[1, 2, -4], [4, 6, 10], [-1, 7, 13]]
#     b_tmp = [3, 7, 1]
#     c_tmp = [1, 3, 2, -1]  # the last is free coefficient
#     A_signs_tmp = ['<=', '=', '>=']
#     x_signs_tmp = [0, 1]
#     min_max_tmp = 'min'
#     ####################
#     M1, M2, N1, N2, min_max_new = manager(c_tmp, A_tmp, b_tmp, A_signs_tmp, min_max_tmp, x_signs_tmp)
#     c_ctmp, A_ctmp, b_ctmp, A_s_ctmp, x_s_ctmp = common_to_canonical(c_tmp, A_tmp, b_tmp, M1, M2, N1, N2, A_signs_tmp)
#     try:
#         gmp1 = sm.calc_global_minimum_point(c_ctmp, A_ctmp, b_ctmp)
#         # print(np.dot(c, gmp))
#         print('\n', gmp1)
#     except sm.SimplexException as ex:
#         print(ex.err_msg)
#
#     eps = pow(10, -1)
#     print(eps)
#     differ_list = list()
#     gmp_tmp = list()
#     gmp_differ = list()
#     eps_list = [pow(10, -1)]
#     for i in range(11):
#         b_canon_tmp = [j+eps for j in b_ctmp]
#         try:
#             gmp_tmp = sm.calc_global_minimum_point(c_ctmp, A_ctmp, b_canon_tmp)
#             # print(np.dot(c, gmp))
#             print('\n', gmp_tmp)
#         except sm.SimplexException as ex:
#             print(ex.err_msg)
#         if i < 10:
#             eps /= 10
#             eps_list.append(eps)
#         print(gmp1)
#         gmp_differ = [gmp1[i] - gmp_tmp[i] for i in range(len(gmp1))]
#         differ_list.append(linalg.norm(gmp_differ, np.inf))
#     print(differ_list)
#     print(eps_list)
#
#     # exponential function x = 10^y
#     datax = [10 ** -i for i in range(10)]
#     datay = [i for i in range(10)]
#
#     # convert x-axis to Logarithmic scale
#     plt.xscale("log")
#     plt.yscale("log")
#     plt.xlabel('delta')
#     plt.ylabel('norma')
#     plt.title('Зависимость решения от возмущений в правой части')
#
#     plt.plot(differ_list, eps_list)
#     plt.show()
# def specialInterface():
#     get_count()
#     get_signs()
#     get_func()
#     get_equations()

# A = [[0, -1, -1, 0, 0], [1, 2, 1, 0, -1], [1, 0, 0, -2, 0], [2, 0, -1, 0, 1], [1, 1, 1, 1, 3]]
# b = [-8, 3, -3, 6, 38]
# c = [8, -4, 5, -6, -6, 0]  # the last is free coefficient
# A_signs = ['>=', '>=', '=', '=', '=']
# x_signs = [0, 1, 2, 3]
# min_max = 'min'
# count_of_variables = len(A[0])
# count_of_equations = len(A)

A = numpy.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
b = numpy.array([33, 35, 17, 12, 23, 34, 5, 16, 19])
c = numpy.array([1, 4, 7, 8, 11, 3, 5, 9, 7, 14, 4, 5, 12, 6, 9, 6, 10, 11, 17, 13, 9999999999999, 9999999999999, 999999999999,
                 99999999999, 999999999999, 999999999999, 999999999999, 999999999999, 999999999999, 999999999999])  # the last is free coefficient
# b = numpy.array([37, 14, 21, 26, 9, 17, 24, 26, 22])
# c = numpy.array([6, 7, 2, 7, 5, 4, 3, 3, 8, 9, 11, 3, 12, 9, 16, 8, 6, 9, 16, 10, 9999999999999, 9999999999999, 999999999999,
#                  99999999999, 999999999999, 999999999999, 999999999999, 999999999999, 999999999999, 999999999999])  # the last is free coefficient
A_signs = numpy.array(['=', '=', '=', '=', '=', '=', '=', '=', '='])
x_signs = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28])
min_max = 'min'

def output_vec(vec, len):
    window = Tk()
    S = "( "
    for i in range(len):
        S += str(vec[i])
        if i != len - 1:
            S += ", "
    S += " )"
    print(S)
    txt = Label(window, text=S, font=("Arial Bold", 20))
    txt.grid(column=0, row=0)
    window.geometry('550x350')
    window.title("")  # сюда можно написать пояснение
    window.mainloop()


def end_of_get_count(spin1, spin2, window):
    global count_of_equations
    global count_of_variables
    count_of_equations = int(spin2.get())
    count_of_variables = int(spin1.get())
    window.destroy()


def get_count():
    window = Tk()

    label1 = Label(window, text="Количество переменных:", font=("Arial Bold", 20))
    label1.grid(column=0, row=0)
    spin1 = Spinbox(window, from_=1, to=100, font=("Arial Bold", 20))
    spin1.grid(column=0, row=1)
    label2 = Label(window, text="Количество уравнений:", font=("Arial Bold", 20))
    label2.grid(column=0, row=2)
    spin2 = Spinbox(window, from_=1, to=100, font=("Arial Bold", 20))
    spin2.grid(column=0, row=3)

    click = partial(end_of_get_count, spin1, spin2, window)
    btn = Button(window, text="Готово", command=click, font=("Arial Bold", 20))
    btn.grid(column=0, row=4)

    window.geometry('550x350')
    window.title("")
    window.mainloop()


def end_of_get_signs(signs, window):
    i = 0
    global x_signs
    x_signs = []
    for sign in signs:
        if sign.get() == ">=0":
            x_signs.append(i)
        i += 1
    window.destroy()


def get_signs():
    window = Tk()
    signs = []

    text = Label(window, text="Какие переменные >= 0?", font=("Arial Bold", 15))
    text.grid(column=0, row=0)

    for i in range(count_of_variables):
        sign = Combobox(window, font=("Arial Bold", 15))
        sign['values'] = (">=0", "Без ограничений")
        sign.grid(column=1, row=i + 1)
        signs.append(sign)

        text = Label(window, text="x" + str(i + 1), font=("Arial Bold", 15), width=3)
        text.grid(column=0, row=i + 1)

    click = partial(end_of_get_signs, signs, window)
    btn = Button(window, text="Готово", command=click, font=("Arial Bold", 15))
    btn.grid(column=0, row=count_of_variables + 1)

    window.geometry('550x350')
    window.title("")
    window.mainloop()


def end_of_get_func(ratios, minormax, window):
    global c
    c = []
    global min_max
    for ratio in ratios:
        c.append(float(ratio.get()))
    min_max = minormax.get()
    window.destroy()


def get_func():
    ratios = []

    window = Tk()
    for i in range(count_of_variables):
        ratio = Entry(window, width=5, font=("Arial Bold", 15))
        ratio.grid(column=i * 2, row=0)
        ratios.append(ratio)

        txt = Label(window, text="x" + str(i + 1) + " + ", font=("Arial Bold", 15))
        txt.grid(column=i * 2 + 1, row=0)

    free = Entry(window, width=5, font=("Arial Bold", 15))
    free.grid(column=count_of_variables * 2, row=0)
    ratios.append(free)

    txt = Label(window, text=" --> ", font=("Arial Bold", 15))
    txt.grid(column=count_of_variables * 2 + 1, row=0)

    min_or_max = Combobox(window, font=("Arial Bold", 15), width=5)
    min_or_max['values'] = ("min", "max")
    min_or_max.grid(column=count_of_variables * 2 + 2, row=0)

    click = partial(end_of_get_func, ratios, min_or_max, window)
    btn = Button(window, text="Готово", command=click, font=("Arial Bold", 15))
    btn.grid(column=0, row=1)
    window.geometry('550x350')
    window.title("")
    window.mainloop()


def end_of_get_equations(equations, right_side, signs, window):
    global A
    A = []
    global b
    b = []
    global A_signs
    A_signs = []
    for equation in equations:
        a = []
        for ratio in equation:
            a.append(float(ratio.get()))
        A.append(a)

    for ratio in right_side:
        b.append(float(ratio.get()))

    for sign in signs:
        A_signs.append(sign.get())
    window.destroy()


def get_equations():
    window = Tk()
    equations = []
    right_side = []
    signs = []
    for i in range(count_of_equations):
        ratios = []
        for j in range(count_of_variables):
            ratio = Entry(window, width=5, font=("Arial Bold", 15))
            ratio.grid(column=j * 2, row=i)
            ratios.append(ratio)

            S = ""
            if j == count_of_variables - 1:
                S = "x" + str(j + 1)
            else:
                S = "x" + str(j + 1) + " + "
            txt = Label(window, text=S, font=("Arial Bold", 15))
            txt.grid(column=j * 2 + 1, row=i)

        sign = Combobox(window, font=("Arial Bold", 15), width=3)
        sign['values'] = ("<=", ">=", "=")
        sign.grid(column=count_of_variables * 2, row=i)

        b = Entry(window, width=5, font=("Arial Bold", 15))
        b.grid(column=count_of_variables * 2 + 2, row=i)

        right_side.append(b)
        equations.append(ratios)
        signs.append(sign)

        click = partial(end_of_get_equations, equations, right_side, signs, window)
        btn = Button(window, text="Готово", command=click, font=("Arial Bold", 15))
        btn.grid(column=0, row=count_of_equations)

    window.geometry('550x350')
    window.title("")
    window.mainloop()


if __name__ == '__main__':
    # A = [[1, 2, -4], [4, 6, 10], [-1, 7, 13]]
    # b = [3, 7, 1]
    # c = [1, 3, 2, -1]  # the last is free coefficient
    # A_signs = ['<=', '=', '>=']
    # x_signs = [0, 1]
    # min_max = 'max'

    # get_count()
    # print(count_of_equations, count_of_variables)
    # get_signs()
    # print(x_signs)
    # get_func()
    # print(c)
    # get_equations()
    # print(A)
    # print(A_signs)

    # printing(c, A, b, A_signs, min_max, x_signs)

    M1, M2, N1, N2, min_max_new = manager(c, A, b, A_signs, min_max, x_signs)

    printing(c, A, b, A_signs, min_max_new, x_signs)
    # print(M1, M2, N1, N2, sep='\n')

    # c_canon, A_canon, b_canon, A_signs_canon, x_signs_canon = common_to_canonical(c, A, b, M1, M2, N1, N2, A_signs)
    #
    # printing(c_canon, A_canon, b_canon, A_signs_canon, min_max_new, x_signs_canon)

    # A_d, b_d, c_d, A_signs_d, min_max_d, x_signs_d = manager_d(A, b, c, A_signs, min_max_new, x_signs)
    #
    # printing(c_d, A_d, b_d, A_signs_d, min_max_d, x_signs_d)
    #
    # M1_d, M2_d, N1_d, N2_d, min_max_d_new = manager(c_d, A_d, b_d, A_signs_d, min_max_d, x_signs_d)
    # # print(M1_d, M2_d, N1_d, N2_d)
    # cdc, Adc, bdc, Asignsdc, xsignsdc = common_to_canonical(c_d, A_d, b_d, M1_d, M2_d, N1_d, N2_d, A_signs_d)
    #
    # printing(cdc, Adc, bdc, Asignsdc, min_max_d_new, xsignsdc)
    # c = numpy.array(c)
    # A = numpy.array(A)
    # b = numpy.array(b)

    try:
        gmp = sm.calc_global_minimum_point(c, A, b)
        sum = 0
        print(gmp, sep='\n')
        for i in range(len(gmp)):
            sum += int(gmp[i]) * c[i]
        print('\n', sum, '\n')
        # print(np.dot(c, gmp))
        # print('\n', gmp)
        # output_vec(gmp, len(gmp))
    except sm.SimplexException as ex:
        print(ex.err_msg)

    # try:
    #     gmp_d = sm.calc_global_minimum_point(cdc, Adc, bdc)
    #     # print(np.dot(c, gmp))
    #     print('\n', gmp_d)
    # except sm.SimplexException as ex:
    #     print(ex.err_msg)
