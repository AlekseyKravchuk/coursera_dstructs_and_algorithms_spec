import numpy
import numpy as np


def simple_normalize(x: numpy.ndarray, _min=None, _max=None) -> tuple:
    if _min is not None and _max is not None:
        return ((x - _min) / (_max - _min)), _min, _max
    else:
        _min, _max = x.min(), x.max()
        return ((x - _min) / (_max - _min)), _min, _max


def rms_normalize(x: numpy.ndarray, _mean=None, s_x=None) -> tuple:
    # TODO: выполнить нормализацию данных для задания https://stepik.org/lesson/573087/step/7?unit=567636
    """ Normalizing using rms (root mean square)

    :param x: numpy.ndarray
    :param _mean: float, optional, mean value, its needed in case of normalizing single object belonging to test set
    :param s_x: float, optional, its needed in case of normalizing single object belonging to test set
    :return: tuple t: t[0] is normalized feature X, t[1], t[2] are quantitative characteristics
                    used when normalizing train set
    """
    if _mean is not None and s_x is not None:
        return ((x - _mean) / s_x), _mean, s_x
    else:
        _mean = x.mean()
        s_x = np.sqrt((1 / (len(x) - 1)) * (x - _mean) ** 2)
        return (x - _mean) / s_x, _mean, s_x


if __name__ == '__main__':
    # x = np.arange(1, 5)
    x = np.array([50, 60, 80, 100])

    # x_normalized, _min, _max = simple_normalize(x)
    x_normalized, _mean, sigma = rms_normalize(x)
    # print(f'x_normalized = {x_normalized}')
    with np.printoptions(precision=3, suppress=True):
        print(f'x_normalized = {x_normalized}')
        print(f'object_normalized = {rms_normalize(np.array([90]), _mean, sigma)}')
