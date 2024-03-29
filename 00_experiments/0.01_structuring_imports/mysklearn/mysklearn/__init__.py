"""Importing subpackages"""

# Absolute import:
# from mysklearn import preprocessing
# from mysklearn import regression

# Relative import
from . import preprocessing  # from the current directory import "preprocessing" module
from . import regression  # from the current directory import "regression" module
from .utils import MyException

# from preprocessing import normalize, standardize


