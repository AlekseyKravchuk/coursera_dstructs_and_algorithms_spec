# Absolute import
# from mysklearn.preprocessing.funcs import my_max, my_min

from .funcs import my_min, my_max
# Relative import
from .funcs import (my_max, my_min)


def normalize_data():
    print(f'Function "{normalize_data.__name__}()" is called.')
    print('Trying to call functions from sibling module ...')

    print(my_max(10, 5))
    print(my_min(10, 5))


if __name__ == '__main__':
    print(f'Check for normalize_data() ...')
    normalize_data()


