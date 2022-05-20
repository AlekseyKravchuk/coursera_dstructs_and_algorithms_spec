"""Solution to stepik.org course: https://stepik.org/lesson/573082/step/3?unit=567631
"""

import sympy as sp
import numpy as np
import random


if __name__ == '__main__':
    w0, w1 = sp.symbols('w0, w1')
    
    # выражение для функции потерь L(w0, w1)
    L = (-w1 + w0 - 1)**2 + w0**2 + (w1 + w0 + 1)**2

    err_squared_terms = [(-w1 + w0 - 1)**2, w0**2, (w1 + w0 + 1)**2]
    print(f'err_squared_terms = {err_squared_terms}')

    mb1 = err_squared_terms[0] + err_squared_terms[1]  # mini-batch #1
    mb2 = err_squared_terms[1] + err_squared_terms[2]  # mini-batch #2

    # print(f'mini_batch_1 = {mb1}')
    # print(f'mini_batch_2 = {mb2}')

    mb1_grad = np.array([sp.lambdify((w0, w1), sp.diff(mb1, w0)),
                         sp.lambdify((w0, w1), sp.diff(mb1, w1))])

    mb2_grad = np.array([sp.lambdify((w0, w1), sp.diff(mb2, w0)),
                         sp.lambdify((w0, w1), sp.diff(mb2, w1))])
    
    # gradient descent initialization
    a = np.array([0.0, 0.0])
    h = 0.1

    # step #1
    a = a - h * np.array([mb1_grad[0](*a), mb1_grad[1](*a)])

    # step #2
    a = a - h * np.array([mb2_grad[0](*a), mb2_grad[1](*a)])
    print(a)



