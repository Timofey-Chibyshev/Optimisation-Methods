import numpy as np
import grad1
import grad2
import task_data as td

x_from, x_to = -2.0, 2.0
y_from, y_to = -2.0, 2.0


x_start_grad_1 = np.array([-0.25, -0.5])
(x_min_grad_1, points_grad_1) = grad1.calc_min(x_start=x_start_grad_1, grad_eps=0.0001)
print("Last point: ", points_grad_1[-1])
print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_1[-1]), ord=2))
print("Points number: ", len(points_grad_1))


x_start_grad_2 = np.array([-0.25, -0.5])
(x_min_grad_2, points_grad_2) = grad2.calc_min(x_start=x_start_grad_2,
                                               eps=0.001,
                                               alpha_start=0.5,
                                               grad_eps=0.01)
print("Last point: ", points_grad_2[-1])
print("Last gradient norm: ", np.linalg.norm(td.calc_grad(points_grad_2[-1]), ord=2))
print("Points number: ", len(points_grad_2))
