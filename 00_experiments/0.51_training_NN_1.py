import numpy as np

# First we set the state of the network
σ = np.tanh
w1 = -5
b1 = 5


# Then we define the neuron activation.
def a1(a0):
    z = w1 * a0 + b1
    return σ(z)


def C(a1, y):
    return (a1 - y) ** 2


# Experiment with different values of x below.
if __name__ == '__main__':
    x = 1
    y = 0
    a_1 = a1(x)
    cost = C(a_1, y)
    print(f'x = {x}, y = {y}, a1(x) = {a_1:.3f}')
    print(f'C = {cost:.3f}')
