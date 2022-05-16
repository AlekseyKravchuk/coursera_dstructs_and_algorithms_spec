import signal
import time
# from functools import wraps


def timeout(n_seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            #  signal.alarm(time) - Если значение 'time' не равно нулю, эта функция запрашивает передачу сигнала
            #  'SIGALRM' в процесс через 'time' секунд
            signal.alarm(n_seconds)
            try:
                # call the decorated function 'func'
                return func(*args, *kwargs)
            finally:
                # cancel alarm
                signal.alarm(0)
        return wrapper
    return decorator


@timeout(5)
def foo():
    time.sleep(10)
    print('foo!')


@timeout(20)
def bar():
    time.sleep(10)
    print(f'bar!')


def raise_timeout(*args, **kwargs):
    raise TimeoutError()


if __name__ == '__main__':
    # when signal whose number is 'signal.SIGALRM', call the handler function
    # signal.signal)() позволяет определять пользовательские обработчики, которые будут выполнены, когда сигнал получен
    signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)

    foo()
    # bar()

