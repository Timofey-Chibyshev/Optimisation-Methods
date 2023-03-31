from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from functools import partial
import numpy as np
from ConverterLP import *
from ConverterDualTask import *
from ConverterDualTask import *
from SimplexMethod import *
import SimplexMethod as sm
import numpy as np


# A = [[0, -1, -1, 0, 0], [1, 2, 1, 0, -1], [1, 0, 0, -2, 0], [2, 0, -1, 0, 1], [1, 1, 1, 1, 3]]
# b = [-8, 3, -3, 6, 38]
# c = [8, -4, 5, -6, -6, 0]  # the last is free coefficient
# A_signs = ['>=', '>=', '=', '=', '=']
# x_signs = [0, 1, 2, 3]
# min_max = 'min'
# A = []
# b = []
# c = []  # the last is free coefficient
# A_signs = []
# x_signs = []
# min_max = ''
#
# count_of_variables = len(A[0])
# count_of_equations = len(A)

def output_vec(vec, len):
    window = Tk()
    S = "( "
    for i in range(len):
        S+= str(vec[i])
        if i != len-1:
            S+= ", "
    S += " )"
    print(S)
    txt = Label(window, text=S, font=("Arial Bold", 20))
    txt.grid(column=0, row=0)
    window.geometry('550x350')
    window.title("") # сюда можно написать пояснение
    window.mainloop()


# def start():
#     window = Tk()
#
#
#     Afield = Label(window, text="Ограничения:", font=("Arial Bold", 15))
#     Afield.grid(column=0, row=0)
#     for i in range(count_of_equations):
#         for j in range(count_of_variables):
#             S = str(A[i][j]) + " x" + str(j+1)
#             if j != count_of_variables - 1:
#                 S = S + " + "
#             txt = Label(window, text=S, font=("Arial Bold", 15))
#             txt.grid(column=j+1, row=i+1)
#         sign = Label(window, text=str(A_signs[i]) + " " + str(b[i]), font=("Arial Bold", 15))
#         sign.grid(column=count_of_variables+1, row=i+1)
#
#     target = Label(window, text="Функция:", font=("Arial Bold", 15))
#     target.grid(column=0, row=count_of_equations+1)
#     for i in range(count_of_variables+1):
#         S = str(c[i])
#         if i != count_of_variables:
#             S +=" x" + str(i + 1)
#         if i != count_of_variables:
#             S = S + " + "
#         txt = Label(window, text=S, font=("Arial Bold", 15))
#         txt.grid(column=i+1, row = count_of_equations+2)
#     txt = Label(window, text="->"+min_max, font=("Arial Bold", 15))
#     txt.grid(column=count_of_variables+2, row=count_of_equations+2)
#
#
#
#
#     window.geometry('550x350')
#     window.title("Вы хотите изменить текущие данные?")
#     window.mainloop()

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
    spin1 = Spinbox(window, from_ = 1, to=100, font=("Arial Bold", 20))
    spin1.grid(column=0, row=1)
    label2 = Label(window, text="Количество уравнений:", font=("Arial Bold", 20))
    label2.grid(column=0, row=2)
    spin2 = Spinbox(window, from_ = 1, to=100, font=("Arial Bold", 20))
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
        sign.grid(column=1, row=i+1)
        signs.append(sign)

        text = Label(window, text="x"+str(i+1), font=("Arial Bold", 15), width=3)
        text.grid(column=0, row=i+1)

    click = partial(end_of_get_signs, signs, window)
    btn = Button(window, text="Готово", command=click, font=("Arial Bold", 15))
    btn.grid(column=0, row=count_of_variables+1)



    window.geometry('550x350')
    window.title("")
    window.mainloop()


def end_of_get_func(ratios, minormax, window):
    global c
    global min_max
    for ratio in ratios:
        c.append(float(ratio.get()))
    min_or_max = minormax.get()
    window.destroy()

def get_func():
    ratios = []

    window = Tk()
    for i in range(count_of_variables):
        ratio = Entry(window, width=5, font=("Arial Bold", 15))
        ratio.grid(column=i*2, row=0)
        ratios.append(ratio)

        txt = Label(window, text="x"+str(i+1)+" + ", font=("Arial Bold", 15))
        txt.grid(column=i*2+1, row=0)

    free = Entry(window, width=5, font=("Arial Bold", 15))
    free.grid(column=count_of_variables*2, row=0)
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
    global b
    global A_signs
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
            ratio.grid(column=j*2, row=i)
            ratios.append(ratio)

            S = ""
            if j == count_of_variables - 1:
                S = "x" + str(j + 1)
            else:
                S = "x" + str(j + 1) + " + "
            txt = Label(window, text=S, font=("Arial Bold", 15))
            txt.grid(column=j*2 + 1, row=i)





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


if __name__ == "__main__":

    get_count()

    get_signs()

    get_func()

    get_equations()

    M1, M2, N1, N2, min_max_new = manager(c, A, b, A_signs, min_max, x_signs)

    printing(c, A, b, A_signs, min_max_new, x_signs)
    # print(M1, M2, N1, N2, sep='\n')

    c_canon, A_canon, b_canon, A_signs_canon, x_signs_canon = common_to_canonical(c, A, b, M1, M2, N1, N2, A_signs)

    printing(c_canon, A_canon, b_canon, A_signs_canon, min_max_new, x_signs_canon)

    try:
        gmp = sm.calc_global_minimum_point(c_canon, A_canon, b_canon)
        # print(np.dot(c, gmp))
        print('\n', gmp)
    except sm.SimplexException as ex:
        print(ex.err_msg)