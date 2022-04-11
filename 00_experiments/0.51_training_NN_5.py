import numpy as np

sigma = np.tanh  # Define the activation function.


def a1(w1, a_0, b1) :
    z = w1 * a_0 + b1
    return sigma(z)


def Cost(a_1, y):
    return (a_1 - y)**2


if __name__ == '__main__':
    w1 = 1.3
    b1 = -0.1

    a_0 = 0
    y_0 = 1

    a_1 = a1(w1, a_0, b1)
    print(f'C = {Cost(a_1, y_0)}')
