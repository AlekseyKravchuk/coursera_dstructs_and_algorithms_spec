import numpy as np


def fnn(x: np.ndarray) -> np.ndarray:
    return (x - 1) * (x - 2) * (x - 3) * (x - 4)


if __name__ == '__main__':
    # initial values in validation set
    data = np.array([1.5, 2.5, 3.5])

    # true values of the target feature
    target_true = np.array([0.0, 0.0, 0.0])

    # calculate predicted values by passing initial values into NN function0.72_mae.py
    predicted = fnn(data)

    mae = np.sum(np.abs(target_true - predicted)) / len(data)
    print(f'mae = {mae}')

