import doctest


def square(x):
    """Square the number x

    :param x: number to square
    :return: x squared

    >>> square(3)
    9
    """
    return x ** x


if __name__ == '__main__':
    doctest.testmod()

