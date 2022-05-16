import time
from functools import wraps


def timer(func):
    """ A decorator that prints how long a function took to run. """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # When the wrapper is called, get the current time.
        t_start = time.time()

        # call the decorated function and store the result
        res = func(*args, **kwargs)

        # After calling the decorated function, wrapper() checks the time again
        t_elapsed = time.time() - t_start

        print(f'running "{func.__name__}()" took {t_elapsed} seconds.')
        return res

    return wrapper


@timer
def sleep_n_seconds(n):
    time.sleep(n)


if __name__ == '__main__':
    n = 2
    sleep_n_seconds(n)
    print(sleep_n_seconds.__name__)
    print(sleep_n_seconds.__doc__)
    print(sleep_n_seconds.__defaults__)
