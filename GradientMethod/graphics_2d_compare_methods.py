import numpy as np
# import grad1
import SecondOrderGradient as grad2
import task_data as td
import matplotlib.pyplot as plt

x_from, x_to = -2.0, 2.0
y_from, y_to = -2.0, 2.0


''' 
        Counting 'q' for second order method with eps_iter = [10^0, ..., 10^(-5)]   
                                                                                    '''
x_start_grad_2 = np.array([-0.25, -0.5])
(x_min_grad_true, points_grad_true) = grad2.calc_min(x_start=x_start_grad_2,
                                               eps=0.001,
                                               alpha_start=1,
                                               grad_eps=10**(-11))

print("Last point: ", points_grad_true[-1])
print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_true[-1]), ord=2))
print("Points number: ", len(points_grad_true))

q = list()
for eps_iter in range(6):
    (x_min_grad_2, points_grad_2) = grad2.calc_min(x_start=x_start_grad_2, eps=0.001, alpha_start=1, grad_eps=10**(-eps_iter))
    q.append(np.linalg.norm(x_min_grad_true - x_min_grad_2, ord=2))

print("Last point: ", points_grad_2[-1])
print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_2[-1]), ord=2))
print("Points number: ", len(points_grad_2))
print("q:", q)



'''
    График зависимости количества итераций от точности
                                                        '''
iters_secondOrder = list()
fact_ac = list()
eps_graph = [10 ** (-i) for i in range(10)]
for eps_iter in eps_graph:
    print(eps_iter)
    (x_min_grad_tmp, points_grad_tmp) = grad2.calc_min(x_start=x_start_grad_2, eps=0.001, alpha_start=1, grad_eps=eps_iter)
    print("Количество точек:", points_grad_tmp)
    iters_secondOrder.append(len(points_grad_tmp))
    fact_ac.append(np.linalg.norm(x_min_grad_tmp - x_min_grad_true, ord=2))

# ВАНЯ ТУТ СВОЙ ЕЩЕ ВПИШЕТ
fig_eps = plt.figure()
ax_eps = fig_eps.add_subplot(1, 1, 1)

ax_eps.semilogx(eps_graph, iters_secondOrder, label='Метод второго порядка')
# ax_eps.semilogx(eps_graph, iters_VANYA, label='Метод первого порядка')
ax_eps.grid()
ax_eps.set_ylabel('iters')  # Add an x-label to the axes.
ax_eps.set_xlabel('eps')  # Add a y-label to the axes.
ax_eps.set_title("График зависимости количества итераций от точности.")  # Add a title to the axes.
ax_eps.legend()
plt.show()


'''
    График зависимости фактической точности от заданной точности
                                                                '''
fig_fac = plt.figure()
ax_fac = fig_fac.add_subplot(1, 1, 1)

ax_fac.loglog(eps_graph, fact_ac, label='Метод второго порядка')
# ax_fac.loglog(eps_graph, fact_ac_VANYA, label='Метод первого порядка')
ax_fac.grid()
ax_fac.set_ylabel('fact_eps')  # Add an x-label to the axes.
ax_fac.set_xlabel('eps')  # Add a y-label to the axes.
ax_fac.set_title("График зависимости фактической точности от заданной точности.")  # Add a title to the axes.
ax_fac.legend()
plt.show()


'''
    График зависимости количества итераций от точности внутреннего метода
                                                                            '''
# зафиксируем внешнюю точность, например, eps_iternal = 10**(-6)
eps_external = 10**(-6)
iters_per_ac = list()
for eps_iter in eps_graph:
    print(eps_iter)
    (x_min_grad_tmp, points_grad_tmp) = grad2.calc_min(x_start=x_start_grad_2, eps=eps_iter, alpha_start=1, grad_eps=eps_external)
    print("Количество точек:", points_grad_tmp)
    iters_per_ac.append(len(points_grad_tmp))

fig_3 = plt.figure()
ax_3 = fig_3.add_subplot(1, 1, 1)

ax_3.semilogx(eps_graph, iters_per_ac, label='Метод второго порядка')
ax_3.grid()
ax_3.set_ylabel('iters')  # Add an x-label to the axes.
ax_3.set_xlabel('eps_iternal')  # Add a y-label to the axes.
ax_3.set_title("Зависимость количества итераций от точности внутреннего метода.")  # Add a title to the axes.
ax_3.legend()
plt.show()

