# import mysklearn.preprocessing.normalize
import os
import sys

# import mysklearn
from mysklearn.regression.regression import regression_func

if __name__ == '__main__':
    # Lines below will cause error without specifying internal imports in __init__.py
    # print(help(mysklearn.preprocessing))
    # print(help(mysklearn.regression))
    # print(help(mysklearn.regression.regression))
    #
    # dir_path = os.path.dirname(os.path.realpath(__file__))

    # Playing with discovering some paths
    # print(f'dir_path is {dir_path}')
    # print("script: sys.argv[0] is", repr(sys.argv[0]))
    # print("script: __file__ is", repr(__file__))
    # print("script: cwd is", repr(os.getcwd()))

    regression_func()


