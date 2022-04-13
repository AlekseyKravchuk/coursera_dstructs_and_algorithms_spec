import numpy as np
import matplotlib.pyplot as plt


# Here is the activation function and its derivative.
sigma = lambda z: 1 / (1 + np.exp(-z))
d_sigma = lambda z: np.cosh(z/2)**(-2) / 4


# This function initialises the network with it's structure, it also resets any training already done.
# n1=6 is the number of neurons in 2-nd hidden layer (1-st if starting indexing from 0)
# n2=7 is the number of neurons in 3-rd hidden layer (2-nd if starting indexing from 0)
def reset_network(n1=6, n2=7):
    global W1, W2, W3, b1, b2, b3
    W1 = np.random.randn(n1, 1) / 2   # W1_dim = 6x1 = n1x1
    W2 = np.random.randn(n2, n1) / 2  # W2_dim = 7x6 = n2xn1
    W3 = np.random.randn(2, n2) / 2   # W3_dim = 2x7 = n2xn1
    b1 = np.random.randn(n1, 1) / 2   # b1_dim = 6x1 = n1x1
    b2 = np.random.randn(n2, 1) / 2   # b2_dim = 6x1 = n1x1
    b3 = np.random.randn(2, 1) / 2    # b3_dim = 2x1 = 2x1


# This function feeds forward each activation to the next layer. It returns all weighted sums and activations.
def network_function(a0):
    z1 = W1 @ a0 + b1
    a1 = sigma(z1)

    z2 = W2 @ a1 + b2
    a2 = sigma(z2)

    z3 = W3 @ a2 + b3
    a3 = sigma(z3)
    return a0, z1, a1, z2, a2, z3, a3


# This is the cost function of a neural network with respect to a training set.
# 'x' = a0 is the input to neural network
# 'y' is desired output, has the same dimension as vector 'x'
def cost(x, y):
    a3 = network_function(x)[-1]   # a3 is calculated output of NN
    return np.linalg.norm(a3 - y)**2 / x.size


# Jacobian for the third layer weights.
def J_W3(x, y) :
    # First get all the activations and weighted sums at each layer of the network.
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)

    # We'll use the variable J to store parts of our result as we go along, updating it in each line.
    # Firstly, we calculate dC/da3, using the expressions above.
    J = 2 * (a3 - y)     # dC/da3

    # Next multiply the result we've calculated by the derivative of sigma, evaluated at z3.
    J = J * d_sigma(z3)  # da3/dz3

    # Then we take the dot product (along the axis that holds the training examples) with the final partial derivative,
    # i.e. dz3/dW3 = a2
    # and divide by the number of training examples, for the average over all training examples.
    J = J @ a2.T / x.size   # dz3/dW3 = a2
    # Finally return the result out of the function.
    return J


# In this function, you will implement the jacobian for the bias.
# As you will see from the partial derivatives, only the last partial derivative is different.
# The first two partial derivatives are the same as previously.
# ===YOU SHOULD EDIT THIS FUNCTION===
def J_b3(x, y) :
    # As last time, we'll first set up the activations.
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)      # dC/da3
    J = J * d_sigma(z3)   # da3/dz3
    # For the final line, we don't need to multiply by dz3/db3, because that is multiplying by 1.
    # We still need to sum over all training examples however.
    # There is no need to edit this line.
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J


# Compare this function to J_W3 to see how it changes.
# There is no need to edit this function.
def J_W2 (x, y) :
    #The first two lines are identical to in J_W3.
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)     # dC/da3

    # the next two lines implement da3/da2, first σ' and then W3.
    J = J * d_sigma(z3)  # σ'(z3)
    J = (J.T @ W3).T     # W3

    # then the final lines are the same as in J_W3 but with the layer number bumped down.
    J = J * d_sigma(z2)     # da2/dz2 = σ'(z2)
    J = J @ a1.T / x.size   # dz2/dW2 = a1
    return J


# As previously, fill in all the incomplete lines.
# ===YOU SHOULD EDIT THIS FUNCTION===
def J_b2 (x, y) :
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)

    J = J * d_sigma(z3)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J


def J_W1 (x, y) :
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J =(J.T @ W2).T
    J = J * d_sigma(z1)
    J = J @ a0.T / x.size
    return J


def J_b1 (x, y) :
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J =(J.T @ W2).T
    J = J * d_sigma(z1)
    J = J @ a0.T / x.size
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J


if __name__ == '__main__':
    training_data = (np.array([0., 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09,
                               0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19,
                               0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29,
                               0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39,
                               0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49,
                               0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59,
                               0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69,
                               0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79,
                               0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89,
                               0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]),
                     np.array([[0.5, 0.50009902, 0.50078751, 0.50263171, 0.50615226,
                                0.5118034, 0.51995466, 0.53087547, 0.54472343, 0.56153657,
                                0.58122992, 0.60359653, 0.62831281, 0.65494819, 0.68297861,
                                0.7118034, 0.74076505, 0.76917106, 0.7963171, 0.82151087,
                                0.84409548, 0.86347181, 0.87911897, 0.89061206, 0.89763674,
                                0.9, 0.89763674, 0.89061206, 0.87911897, 0.86347181,
                                0.84409548, 0.82151087, 0.7963171, 0.76917106, 0.74076505,
                                0.7118034, 0.68297861, 0.65494819, 0.62831281, 0.60359653,
                                0.58122992, 0.56153657, 0.54472343, 0.53087547, 0.51995466,
                                0.5118034, 0.50615226, 0.50263171, 0.50078751, 0.50009902,
                                0.5, 0.49990098, 0.49921249, 0.49736829, 0.49384774,
                                0.4881966, 0.48004534, 0.46912453, 0.45527657, 0.43846343,
                                0.41877008, 0.39640347, 0.37168719, 0.34505181, 0.31702139,
                                0.2881966, 0.25923495, 0.23082894, 0.2036829, 0.17848913,
                                0.15590452, 0.13652819, 0.12088103, 0.10938794, 0.10236326,
                                0.1, 0.10236326, 0.10938794, 0.12088103, 0.13652819,
                                0.15590452, 0.17848913, 0.2036829, 0.23082894, 0.25923495,
                                0.2881966, 0.31702139, 0.34505181, 0.37168719, 0.39640347,
                                0.41877008, 0.43846343, 0.45527657, 0.46912453, 0.48004534,
                                0.4881966, 0.49384774, 0.49736829, 0.49921249, 0.49990098],
                               [0.625, 0.62701541, 0.63296789, 0.64258068, 0.65540709,
                                0.67085156, 0.68819755, 0.70664083, 0.72532628, 0.74338643,
                                0.75997967, 0.77432624, 0.78574006, 0.79365515, 0.79764521,
                                0.79743558, 0.79290745, 0.78409411, 0.77116996, 0.75443315,
                                0.73428307, 0.71119423, 0.68568811, 0.65830476, 0.62957574,
                                0.6, 0.57002377, 0.5400257, 0.51030758, 0.4810911,
                                0.45252033, 0.42466948, 0.3975551, 0.37115155, 0.34540857,
                                0.32026952, 0.29568895, 0.27164821, 0.24816805, 0.22531726,
                                0.20321693, 0.18203995, 0.16200599, 0.14337224, 0.12642077,
                                0.11144335, 0.0987249, 0.08852676, 0.08107098, 0.07652676,
                                0.075, 0.07652676, 0.08107098, 0.08852676, 0.0987249,
                                0.11144335, 0.12642077, 0.14337224, 0.16200599, 0.18203995,
                                0.20321693, 0.22531726, 0.24816805, 0.27164821, 0.29568895,
                                0.32026952, 0.34540857, 0.37115155, 0.3975551, 0.42466948,
                                0.45252033, 0.4810911, 0.51030758, 0.5400257, 0.57002377,
                                0.6, 0.62957574, 0.65830476, 0.68568811, 0.71119423,
                                0.73428307, 0.75443315, 0.77116996, 0.78409411, 0.79290745,
                                0.79743558, 0.79764521, 0.79365515, 0.78574006, 0.77432624,
                                0.75997967, 0.74338643, 0.72532628, 0.70664083, 0.68819755,
                                0.67085156, 0.65540709, 0.64258068, 0.63296789, 0.62701541]]))
    x, y = training_data
    reset_network()
    pass


