"""Solution to stepik.org course: https://stepik.org/lesson/573083/step/1?unit=567632"""

# TODO: реализовать вычисление функции потерь с помощью SymPy

import sympy as sp
import numpy as np


# def grad(x):
#     return np.array([dL_dw0(x[0], x[1]), dL_dw1(x[0], x[1])])


def f(x):  # ReLU function
    return max(0, x)


if __name__ == '__main__':
    # w11, w12, w21, w22 = sp.symbols('w11, w12, w21, w22')
    # w11, w12, w21, w22 = 0.5, -0.5, -0.5, 0.5
    w11, w12, w21, w22 = sp.symbols('w11, w12, w21, w22')
    # F_0_0 = 0
    # F_0_1 = f(f(w21) + f(w22))
    # F_1_0 = f(f(w11) + f(w12))
    # F_1_1 = f(f(f(w11 + w21) + f(w12 + w22)))

    # (F(0,0) - 0)**2 = 0
    # L = (F_0_1 - 1)**2 + (F_1_0 - 1)**2 + (F_1_1 - 0)**2
    L = (f(f(w21) + f(w22)) - 1) ** 2 + (f(f(w11) + f(w12)) - 1) ** 2 + (f(f(f(w11 + w21) + f(w12 + w22))) - 0) ** 2
    dL_dw11 = sp.diff(L, w11)
    print(f'dL_dw11 = {dL_dw11}')

    # print(f'F_0_0 = {F_0_0}\n'
    #       f'F_0_1 = {F_0_1}\n'
    #       f'F_1_0 = {F_1_0}\n'
    #       f'F_1_1 = {F_1_1}')
