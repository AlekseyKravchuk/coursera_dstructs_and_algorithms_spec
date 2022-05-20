"""Solution to stepik.org course: https://stepik.org/lesson/573082/step/2?unit=567631
"""

import sympy as sp
import numpy as np
import random


if __name__ == '__main__':
    w0, w1 = sp.symbols('w0, w1')
    
    # выражение для функции потерь L(w0, w1)
    L = (w0 - 1) ** 2 + (w1 + w0 - 2) ** 2 + (2*w1 + w0 - 3) ** 2
    
    # получаем кортеж из слагаемых в L(w0, w1)
    # terms = L.args
    err_squared_terms = [(w0 - 1)**2, (w1 + w0 - 2)**2, (2*w1 + w0 - 3)**2]
    print(f'err_squared_terms = {err_squared_terms}')

    # вычисляем частные производные для каждого из слагаемых функции L(w0, w1) в символьном виде
    # grads_symbolic = [np.array([sp.diff(term, w0), sp.diff(term, w1)]) for term in L.args]
    part_derrs_symbolic = [np.array([sp.diff(term, w0), sp.diff(term, w1)]) for term in err_squared_terms]

    print('================================')
    for diff_symb in part_derrs_symbolic:
        print(f'{diff_symb[0]}, {diff_symb[0]}')
    print('================================')

    # приводим вычисленные частные производные к объектам-функциям
    grads = [np.array([sp.lambdify((w0, w1), part_derr[0]),
                       sp.lambdify((w0, w1), part_derr[1])])
             for part_derr in part_derrs_symbolic]
    
    # задаем количество эпох и другие исходные данные
    a = np.array([0.0, 0.0])
    h = 0.1

    print(f'\ta0: (w0 = {a[0]:.3f}, w1 = {a[1]:.3f})')
    for i in range(2):
        a -= h * np.array([grads[i][0](*a), grads[i][1](*a)])
        print(f'\ta{i+1}: (w0 = {a[0]:.3f}, w1 = {a[1]:.3f})')

