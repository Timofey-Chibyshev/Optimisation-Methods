import PotentialsMethod as pm
import numpy as np

prices = np.array([[ 1, 4,  7,  8,  11],
                   [ 3, 5,  9,  7,  14],
                   [ 4, 5, 12,  6, 9],
                   [ 6, 10, 11, 17, 13]], float)
a = np.array([33, 35, 17, 12], float)
b = np.array([23, 34, 5, 16, 19], float)

try:
    global_minimum_point = pm.calc_global_minimum_point(prices, a, b)
    print(global_minimum_point)
    print(np.dot(prices.flatten(), global_minimum_point))
except pm.PotentialsException as ex:
    print(ex.err_msg)

# multi-product task:

product = ["Яблоки", "Бананы", "Кокосы"]

prices = np.array([[[1, 4,  7,  8,  11],
                   [3, 5,  9,  7,  14],   # яблоки
                   [4, 5, 12, 6, 9],
                   [6, 10, 11, 17, 13]],

                  [[1, 4, 7, 8, 11],
                   [3, 5, 9, 7, 14],       # бананы
                   [4, 5, 12, 6, 9],
                   [6, 10, 11, 17, 13]],

                  [[1, 4, 7, 8, 11],
                   [3, 5, 9, 7, 14],
                   [4, 5, 12, 6, 9],     # кокосы
                   [6, 10, 11, 17, 13]]],

                  float)

a = np.array([[33, 35, 17, 12],
              [33, 35, 15, 14],
              [30, 38, 17, 12]],
             float)

b = np.array([[23, 34, 5, 16, 19],
              [23, 34, 5, 16, 19],
              [23, 34, 5, 16, 19]],
             float)


for i in range(3):
    try:
        global_minimum_point = pm.calc_global_minimum_point(prices[i], a[i], b[i])
        print(product[i] + ":")
        print("Оптимальны план:", end=" ")
        for j in global_minimum_point:
            print(j, end=", ")
        print("\nОбщая стоимость:", end=" ")
        print(np.dot(prices[i].flatten(), global_minimum_point))
        print("\n")
    except pm.PotentialsException as ex:
        print(ex.err_msg)
