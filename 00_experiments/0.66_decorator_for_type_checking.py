def returns(return_type):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            assert type(result) == return_type
            return result

        return wrapper

    return decorator


@returns(dict)
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')
