import numpy as np

# Define the activation function.
sigma = np.tanh

# Let's use a random initial weight and bias.
W = np.array([[-0.94529712, -0.2667356, -0.91219181],
              [ 2.05529992,  1.21797092, 0.22914497]])
b = np.array([0.61273249, 1.6422662])


# define our feed forward function
def a1(a0):
    z = W @ a0 + b
    return sigma(z)


if __name__ == '__main__':
    # Next, if a training example is,
    # x = np.array([0.1, 0.5, 0.6])
    x = np.array([0.7, 0.6, 0.2])
    y = np.array([0.9, 0.6])

    # Then the cost function is,
    d = a1(x) - y  # Vector difference between observed and expected activation
    C = d @ d  # Absolute value squared of the difference.
    print(f'Cost function value: {C:.1f}')
