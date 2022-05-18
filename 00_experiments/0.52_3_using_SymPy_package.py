"""Solution to stepik.org course: https://stepik.org/lesson/573082/step/1?unit=567631"""

import sympy as sp
import numpy as np
import random


if __name__ == '__main__':
    w0, w1 = sp.symbols('w0, w1')
    
    # выражение для функции потерь L(w0, w1)
    L = (-w1 + w0 - 1)**2 + (w0 - 0)**2 + (w1 + w0 - 1) ** 2 + (2*w1 + w0 - 4)**2
    
    # получаем кортеж из слагаемых в L(w0, w1)
    terms = L.args
    
    # вычисляем частные производные для каждого из слагаемых функции L(w0, w1) в символьном виде
    grads_symbolic = [np.array([sp.diff(term, w0), sp.diff(term, w1)]) for term in L.args]

    # приводим вычисленные частные производные к объектам-функциям
    grads = [np.array([sp.utilities.lambdify((w0, w1), sp.diff(term, w0)),
                       sp.utilities.lambdify((w0, w1), sp.diff(term, w1))])
             for term in L.args]
    
    # задаем количество эпох и другие исходные данные
    n_epochs = 5
    a = np.array([0.0, 0.0])
    h = 0.1

    for i_epoch in range(n_epochs):
        print(f'Epoch #{i_epoch+1}:')
        for idx, i in enumerate(random.sample(range(len(grads)), len(grads))):
            print(f'\ta[{idx + i_epoch*len(grads)}]: (w0 = {a[0]:.3f}, w1 = {a[1]:.3f})')
            a -= h * np.array([grads[i][0](*a), grads[i][1](*a)])
