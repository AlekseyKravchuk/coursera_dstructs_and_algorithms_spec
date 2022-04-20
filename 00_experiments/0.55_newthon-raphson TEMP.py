import pandas as pd


def f(x):
    return x ** 6 / 6 - 3 * x ** 4 - 2 * x ** 3 / 3 + 27 * x ** 2 / 2 + 18 * x - 30


def d_f(x):
    return x ** 5 - 12 * x ** 3 - 2 * x ** 2 + 27 * x + 18  # Complete this line with the derivative you have calculated.


if __name__ == '__main__':
    # x = -4.0
    # x = 1.99
    x0 = 1
    x1 = x0 - f(x0)/d_f(x0)
    print(f'x1 = {x1}')

