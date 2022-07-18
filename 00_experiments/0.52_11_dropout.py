"""Solution to stepik.org course: https://stepik.org/lesson/573090/step/2?unit=567639"""

import sympy as sp
import numpy as np


if __name__ == '__main__':
    def grad(a):
        return np.array([dL_dw0(a[0], a[1]), dL_dw1(a[0], a[1])])

    w1, w0 = sp.symbols('w1, w0')

    # L = (w0 - 0) ** 2 + (w0 - 0) ** 2 + (w1 + w0 - 0) ** 2 + (w1 + w0 - 1) ** 2
    L = (w0 - 0) ** 2 + (w0 - 0) ** 2 + (w1 + w0 - 0) ** 2 + (w1 + w0 - 1) ** 2

    # calculate partial derivatives using SymPy package
    dL_dw0 = sp.diff(L, w0)
    dL_dw1 = sp.diff(L, w1)

    # translate partial derivatives (dL_dw0, dL_dw1) that ary merely SymPy expressions into Python functions (lambdify)
    dL_dw0 = sp.utilities.lambdify((w0, w1), dL_dw0)
    dL_dw1 = sp.utilities.lambdify((w0, w1), dL_dw1)

    h = 0.1
    a = np.array([0.2, 0.0]).reshape(2, 1)
    n_iterations = 2
    #
    for i in range(n_iterations+1):
        print(f'a[{i}]: a[0] = {a[0]}, a[1] = {a[1]}')
        a -= h * grad(a)

