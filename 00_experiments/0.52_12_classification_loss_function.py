"""Solution to stepik.org course: https://stepik.org/lesson/573071/step/5?unit=567620"""

import sympy as sp
import numpy as np


def grad(a: np.array, funcs: np.array) -> np.array:
    assert len(a) == len(funcs)

    return np.array([f(*a) for f in funcs])


if __name__ == '__main__':
    w1, w2, w3, w4 = sp.symbols('w1, w2, w3, w4')
    L = -sp.ln(sp.E**(-w1 + w3) / (sp.E**(-w1 + w3) + sp.E**(-w2 + w4))) \
        - sp.ln(sp.E**w4 / (sp.E**w3 + sp.E**w4))\
        - sp.ln(sp.E**(w1 + w3) / (sp.E**(w1 + w3) + sp.E**(w2 + w4)))

    # calculate partial derivatives as SymPy expressions
    dL_dw1 = sp.diff(L, w1)
    dL_dw2 = sp.diff(L, w2)
    dL_dw3 = sp.diff(L, w3)
    dL_dw4 = sp.diff(L, w4)

    # translate partial derivatives (dL_dw1, dL_dw2, dL_dw3, dL_dw4) being SymPy expressions into Python functions
    dL_dw1_f = sp.utilities.lambdify((w1, w2, w3, w4), dL_dw1)
    dL_dw2_f = sp.utilities.lambdify((w1, w2, w3, w4), dL_dw2)
    dL_dw3_f = sp.utilities.lambdify((w1, w2, w3, w4), dL_dw3)
    dL_dw4_f = sp.utilities.lambdify((w1, w2, w3, w4), dL_dw4)

    funcs = np.array([dL_dw1_f, dL_dw2_f, dL_dw3_f, dL_dw4_f])

    h = 0.1
    a = np.array([0.0, 0.0, 0.0, 0.0]).reshape(4, 1)
    n_iterations = 5

    for i in range(n_iterations):
        if i:
            print(f'After {i} steps of gradient descent vector a = ({a[0]}, {a[1]}, {a[2]}, {a[3]})')
            a -= h * grad(a, funcs)

