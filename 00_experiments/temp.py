import numpy as np

if __name__ == '__main__':
    # a = np.arange(1, 3*3*5+1).reshape(5, 3, 3)
    # print(a)
    #
    #
    # print(f'a.itemsize = {a.itemsize}')
    # print(f'a.strides = {a.strides}')
    # # b = a[:, 0][:, np.newaxis]
    # b = a[:, 0][:, None]
    # print(b)
    # a = np.array([[2, 2, 2],
    #               [2, 2, 2],
    #               [2, 2, 2]])
    a = np.arange(1, 10).reshape(3, 3)
    b = np.array([[3, 3, 3],
                  [3, 3, 3],
                  [3, 3, 3]])
    c = a * b
    print(c)
    print(c.sum())
    print()
    print(c[1:, 1:])