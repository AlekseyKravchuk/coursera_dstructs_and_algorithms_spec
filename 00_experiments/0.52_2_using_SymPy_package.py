"""Solution to stepik.org course: https://stepik.org/lesson/573081/step/3?unit=567630"""

import sympy as sp
import numpy as np


def grad(a):
    return np.array([dL_dw0(a[0], a[1]), dL_dw1(a[0], a[1])])


if __name__ == '__main__':
    w0, w1 = sp.symbols('w0, w1')

    # L(w1, w0) - функция потерь, где w1 - это вес триваиальной NN, а w0 - это смещение (bias)
    # L = (-w1 + w0 - 1) ** 2 + w0 ** 2 + (w1 + w0 + 1) ** 2
    L = (w0 - 1)**2 + (w1 + w0 -2)**2 + (2*w1 + w0 - 3)**2
    # calculate partial derivatives using SymPy package
    dL_dw0 = sp.diff(L, w0)
    dL_dw1 = sp.diff(L, w1)

    # translate partial derivatives (dL_dw0, dL_dw1) that ary merely SymPy expressions into Python functions (lambdify)
    dL_dw0 = sp.utilities.lambdify((w0, w1), dL_dw0)
    dL_dw1 = sp.utilities.lambdify((w0, w1), dL_dw1)

    h = 0.1
    a = np.array([0.0, 0.0]).reshape(2, 1)
    n_iterations = 10

    for i in range(n_iterations):
        print(f'a[{i+1}]: (a[0] = {a[0]}, a[1] = {a[1]})')
        a -= h * grad(a)

    # print(dL_dw0)
    # print(dL_dw1)
