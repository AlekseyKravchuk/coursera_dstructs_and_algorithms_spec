import numpy as np

# First we set the state of the network
σ = np.tanh
w1 = 1.3
b1 = -0.1


# Then we define the neuron activation.
def a1(a0):
    z = w1 * a0 + b1
    return σ(z)


def C(a1, y):
    return (a1 - y) ** 2


# Experiment with different values of x below.
if __name__ == '__main__':
    x = 0
    y = 1
    print(f'x = {x}, a1(x) = {a1(x):.3f}')
    print(f'C = {C(a1(x), y):.3f}')
