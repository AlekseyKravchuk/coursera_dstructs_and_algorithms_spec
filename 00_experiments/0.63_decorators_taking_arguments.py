def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@run_n_times(3)
def print_sum(a, b):
    print(f'{a} + {b} = {a + b}')


@run_n_times(5)
def print_hello():
    print('Hello!')


if __name__ == '__main__':
    # run_three_times = run_n_times(3)
    # print('something happened')

    # print_sum(3, 11)
    # print_hello()

    # without decorator syntax
    # run_three_times = run_n_times(3)
    # wrap_func = run_three_times(print_hello)
    # wrap_func()

    print_sum(11, 18)
