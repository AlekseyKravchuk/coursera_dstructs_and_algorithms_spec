"""Solution to stepik.org course: https://stepik.org/lesson/664910/step/2?unit=662799"""

import sympy as sp
import numpy as np


if __name__ == '__main__':
    def grad(a):
        return np.array([dL_dw1(*a), dL_db1(*a), dL_dw2(*a), dL_db2(*a)])

    def grad_with_first_layers_frozen(a):
        return np.array([np.array([0.0]), np.array([0.0]), dL_dw2(*a), dL_db2(*a)])

    w1, w2, b1, b2 = sp.symbols('w1, w2, b1, b2')
    _w1, _w2, _b1, _b2 = 1.0, 1.0, 1.0, -1.0

    # L(w1, b1, w2, b2) is Loss Function
    L = ((-2*w1 + b1)*w2 + b2 - 4) ** 2 + ((2*w1 + b1)*w2 + b2 - 4) ** 2

    # calculate partial derivatives using SymPy package
    dL_dw1 = sp.diff(L, w1)
    dL_db1 = sp.diff(L, b1)
    dL_dw2 = sp.diff(L, w2)
    dL_db2 = sp.diff(L, b2)

    # translate partial derivatives (dL_dw1, dL_db1, dL_dw2, dL_db2) from SymPy expressions into Python functions
    dL_dw1 = sp.utilities.lambdify((w1, b1, w2, b2), dL_dw1)
    dL_db1 = sp.utilities.lambdify((w1, b1, w2, b2), dL_db1)
    dL_dw2 = sp.utilities.lambdify((w1, b1, w2, b2), dL_dw2)
    dL_db2 = sp.utilities.lambdify((w1, b1, w2, b2), dL_db2)

    # h = 0.1
    h = np.array([0.05, 0.05, 0.1, 0.1]).reshape(4, 1)
    a = np.array([_w1, _w2, _b1, _b2]).reshape(4, 1)
    n_iterations = 5

    for i in range(n_iterations):
        print(f'a[{i+1}]: (w1 = {a[0]}, b1 = {a[1]}, w2 = {a[2]}), b2 = {a[3]}')
        # a -= h * grad_with_first_layers_frozen(a)
        a -= h * grad(a)

    # print(dL_dw0)
    # print(dL_dw1)
