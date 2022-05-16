# Функция - полноправный объект => функция может использоваться как полноправный объект в любых контекстах.
# Внутренняя функция может захватывать (получать доступ) к переменным функции-родителя (external function)


def logger(func):
    def some_wrapper(*args):
        print(f'{func.__name__} started')
        res = func(*args)
        print(f'{func.__name__} finished')
        return res

    return some_wrapper


# декоратор - это просто синтаксический сахар
# при интерпретации интерпретатор попросту заменяет my_sum на обертку, wrapper, которая описана в функции 'logger'
# интерпретатор делает ровно вот это: my_sum = logger(my_sum), в результате функциональный объект 'my_sum' содержит
# ссылку на wrapper 'some_wrapper'
@logger
def my_sum(a, b):
    return a + b


def example_func(func):
    print(f'Name of the called function: {func.__name__}')


if __name__ == '__main__':
    # my_sum = logger(my_sum)
    # print(my_sum)
    # print(my_sum(10, 20))
    # function = logger(my_sum)
    # print(function(5, 30))

    # the same, but less obvious
    # print((logger(my_sum))(5, 20))

    # tmp_fun = logger(my_sum)
    print(my_sum(40, 50))
