from scipy import optimize


def f(x):
    return x ** 6 / 6 - 3 * x ** 4 - 2 * x ** 3 / 3 + 27 * x ** 2 / 2 + 18 * x - 30


if __name__ == '__main__':
    # x0 = -4
    x0 = 3.1
    root = optimize.newton(f, x0)
    print(f'root = {root}')

