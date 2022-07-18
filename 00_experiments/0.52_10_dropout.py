"""Solution to stepik.org course: https://stepik.org/lesson/573090/step/2?unit=567639"""

import sympy as sp
import numpy as np


if __name__ == '__main__':
    def grad(a):
        return np.array([dL_dw02(a[0], a[1]), dL_dw2(a[0], a[1])])

    w2, w02 = sp.symbols('w2, w02')

    L = (w02 - 1)**2 + (w2 + w02 - 2)**2 + (2*w2 + w02 - 3)**2

    # calculate partial derivatives using SymPy package
    dL_dw02 = sp.diff(L, w02)
    dL_dw2 = sp.diff(L, w2)

    # translate partial derivatives (dL_dw0, dL_dw1) that ary merely SymPy expressions into Python functions (lambdify)
    dL_dw02 = sp.utilities.lambdify((w2, w02), dL_dw02)
    dL_dw2 = sp.utilities.lambdify((w2, w02), dL_dw2)

    h = 0.1
    a = np.array([0.0, 0.0]).reshape(2, 1)
    n_iterations = 2
    #
    for i in range(n_iterations):
        print(f'a[{i}]: a[0] = {a[0]}, a[1] = {a[1]}')
        a -= h * grad(a)

    # print(f'dL_dw2 = {dL_dw2}')
    # print(f'dL_dw02 = {dL_dw02}')
