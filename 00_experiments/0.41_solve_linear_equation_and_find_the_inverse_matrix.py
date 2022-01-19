import numpy as np

if __name__ == '__main__':
    # A = np.array([[1, 1, 3],
    #               [1, 2, 4],
    #               [1, 1, 2]])
    # A_inverse = np.linalg.inv(A)
    # print(f'A_inverse = \n{A_inverse}')
    # print(f'check:\nA x A_inverse = \n{A @ A_inverse}')

    # A = np.array([[1, 3/2, 1/2],
    #               [0, 1, 1],
    #               [0, 0, 1]])
    # b = np.array([[9/4, -1/2, 0]]).T
    # x = np.linalg.solve(A, b)
    # print(x)

    # A = np.array([[1, 1, 1],
    #               [3, 2, 1],
    #               [2, 1, 2]])
    # A_inverse = np.linalg.inv(A)
    # print(A_inverse)

    A = np.array([[2, 4, -2],
                  [4, 9, -3],
                  [-2, -3, 7]])
    x = np.array([[-1, 2, 2]])

