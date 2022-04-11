import numpy as np

sigma = np.tanh  # Define the activation function.


if __name__ == '__main__':

    # Let's start with an unfit weight and bias.
    W = np.array([[-2, 4, -1], [6, 0, -3]])
    b = np.array([0.1, -2.5])

    a0 = np.array([0.3, 0.4, 0.1])
    a1 = sigma(W @ a0 + b)
    print(f'a1 = {a1}')
