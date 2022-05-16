# explanation from https://www.youtube.com/watch?v=q4o_1cXAS-c

from functools import wraps


def example(a):
    def inner(b):
        print(f'{a} + {b} = {a + b}')

    inner(5)

    return inner


def logger(func):
    """A decorator that prints started and finished along with function name"""

    @wraps(func)
    def wrapper(a, b):
        print(f'{func.__name__} started.')
        result = func(a, b)
        print(f'{func.__name__} finished.')
        return result

    return wrapper


@logger  # @logger эквивалентно my_sum = logger(my_sum)
def my_sum(a, b):
    return a + b


if __name__ == '__main__':
    # example(2)

    a, b = 2, 5

    # func = logger(my_sum)
    # print(func(a, b))

    # print(logger(my_sum)(a, b))

    # func_obj = logger(my_sum) # переменной func_obj присвоили объект-функцию 'wrapper', которую вернул 'logger'
    # print(func_obj(2, 3))

    # print(my_sum(2, 3))
    print(my_sum.__wrapped__(2, 3))



