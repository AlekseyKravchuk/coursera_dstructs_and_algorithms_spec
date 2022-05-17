"""Solution to stepik.org course: https://stepik.org/lesson/573082/step/1?unit=567631"""

# TODO: реализовать вычисление функции потерь с помощью SymPy

import sympy as sp
import numpy as np


# def grad(x):
#     return np.array([dL_dw0(x[0], x[1]), dL_dw1(x[0], x[1])])


def f(x):  # ReLU function
    return max(0, x)


if __name__ == '__main__':
    w0, w1 = sp.symbols('w0, w1')

    L = (-w1 + w0 - 1)**2 + (w0 - 0)**2 + (w1 + w0 - 1) ** 2 + (2*w1 + w0 - 4)**2

    dl_dw0 = sp.diff(L, w0)
    dl_dw1 = sp.diff(L, w1)

    print(f'dl_dw0 = {dl_dw0}')
    print(f'dl_dw1 = {dl_dw1}')



